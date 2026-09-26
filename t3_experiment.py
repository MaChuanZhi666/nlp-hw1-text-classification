"""Full fine-tuning of bert-base-uncased on the unchanged T1 split.
Run .venv/Scripts/python.exe t3_experiment.py (or --smoke for one training batch).
"""
import os
os.environ.setdefault('TOKENIZERS_PARALLELISM','false')
os.environ.setdefault('CUBLAS_WORKSPACE_CONFIG',':4096:8')
import argparse
import gc
import json
import math
import random
import time
import platform
import numpy as np
import pandas as pd
import torch
import transformers
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, BertForSequenceClassification, get_linear_schedule_with_warmup
from nlp_common import ROOT, CLASSES, load_splits, provenance, scores, evaluate, save_json

OUT=ROOT/'t3_results'
MODEL=ROOT/'models'/'bert-base-uncased'
CONFIG={'epochs':3,'learning_rate':2e-5,'weight_decay':.01,'warmup_ratio':.1,
        'max_length':512,'batch_size':4,'gradient_accumulation':8,'eval_batch_size':8,
        'max_grad_norm':1.0,'seed':42,'long_document':'head 255 + [SEP] + tail 254 with [CLS]/final [SEP]',
        'selection':'highest validation macro_f1, earlier epoch on tie','class_weights':None}

def seed_all():
    random.seed(42);np.random.seed(42);torch.manual_seed(42);torch.cuda.manual_seed_all(42)
    torch.backends.cudnn.deterministic=True
    torch.backends.cudnn.benchmark=False
    torch.set_num_threads(4)

def encode_frames(frames,tokenizer):
    datasets={};stats={};audit=[]
    # No truncation here: full lengths are retained for a measurable truncation audit.
    tokenizer.model_max_length=1000000
    for name,frame in frames.items():
        full=tokenizer(frame.text.tolist(),add_special_tokens=False,truncation=False)['input_ids']
        examples=[];counts=[]
        for i,ids in enumerate(full):
            truncated=len(ids)>CONFIG['max_length']-2
            if truncated:
                first,last=ids[:255],ids[-254:]
                input_ids=tokenizer.build_inputs_with_special_tokens(first,last)
                types=tokenizer.create_token_type_ids_from_sequences(first,last)
                kept=509
            else:
                input_ids=tokenizer.build_inputs_with_special_tokens(ids)
                types=tokenizer.create_token_type_ids_from_sequences(ids)
                kept=len(ids)
            assert len(input_ids)<=CONFIG['max_length']
            examples.append({'input_ids':input_ids,'token_type_ids':types,'attention_mask':[1]*len(input_ids),
                             'labels':CLASSES.index(frame.label.iloc[i])})
            counts.append({'row_id':int(frame.row_id.iloc[i]),'label':frame.label.iloc[i],
                           'wordpieces':len(ids),'retained_wordpieces':kept,'truncated':truncated})
            if name=='test':audit.append({**counts[-1],'visible_input':tokenizer.decode(input_ids)})
        datasets[name]=examples
        c=pd.DataFrame(counts)
        stats[name]={'n':len(c),'mean_wordpieces':float(c.wordpieces.mean()),
            'truncated_n':int(c.truncated.sum()),'truncated_fraction':float(c.truncated.mean()),
            'token_retained_fraction':float(c.retained_wordpieces.sum()/c.wordpieces.sum()),
            'by_class':{label:{'n':int((c.label==label).sum()),'truncated_n':int(c.loc[c.label.eq(label),'truncated'].sum())} for label in CLASSES}}
        print('Tokenized',name,stats[name],flush=True)
    pd.DataFrame(audit).to_csv(OUT/'test_input_audit.csv',index=False)
    return datasets,stats

def main(smoke=False):
    OUT.mkdir(exist_ok=True)
    seed_all()
    assert torch.cuda.is_available(), 'CUDA PyTorch/GPU is required for this training configuration.'
    started=time.perf_counter()
    device=torch.device('cuda')
    amp_dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    scaler=torch.cuda.amp.GradScaler(enabled=amp_dtype==torch.float16)
    frames=load_splits()
    tokenizer=AutoTokenizer.from_pretrained(MODEL,local_files_only=True)
    datasets,stats=encode_frames(frames,tokenizer)
    def collate(examples):return tokenizer.pad(examples,padding=True,pad_to_multiple_of=8,return_tensors='pt')
    generator=torch.Generator().manual_seed(42)
    train_loader=DataLoader(datasets['train'],batch_size=CONFIG['batch_size'],shuffle=True,
        generator=generator,collate_fn=collate,num_workers=0,pin_memory=True)
    loaders={n:DataLoader(datasets[n],batch_size=CONFIG['eval_batch_size'],shuffle=False,
        collate_fn=collate,num_workers=0,pin_memory=True)for n in ['valid','test']}
    model=BertForSequenceClassification.from_pretrained(MODEL,num_labels=3,
        id2label=dict(enumerate(CLASSES)),label2id={c:i for i,c in enumerate(CLASSES)},
        local_files_only=True,attn_implementation='sdpa').to(device)
    decay=[];nodecay=[]
    for name,param in model.named_parameters():
        (nodecay if 'bias' in name or 'LayerNorm.weight' in name else decay).append(param)
    optimizer=torch.optim.AdamW([{'params':decay,'weight_decay':CONFIG['weight_decay']},
                                {'params':nodecay,'weight_decay':0}],lr=CONFIG['learning_rate'],foreach=False)
    updates=math.ceil(len(train_loader)/CONFIG['gradient_accumulation'])*CONFIG['epochs']
    scheduler=get_linear_schedule_with_warmup(optimizer,math.ceil(updates*CONFIG['warmup_ratio']),updates)

    def infer(loader):
        model.eval();all_prob=[];loss_sum=0;n=0
        with torch.inference_mode():
            for batch in loader:
                batch={k:v.to(device,non_blocking=True)for k,v in batch.items()}
                with torch.autocast('cuda',dtype=amp_dtype):output=model(**batch)
                all_prob.append(output.logits.float().softmax(-1).cpu().numpy())
                loss_sum+=float(output.loss)*len(batch['labels']);n+=len(batch['labels'])
        prob=np.concatenate(all_prob)
        pred=np.array(CLASSES)[prob.argmax(axis=1)]
        return pred,prob,loss_sum/n

    result={'provenance':provenance(),'classes':CLASSES,'config':CONFIG,
        'source':json.loads((MODEL/'source.json').read_text(encoding='utf-8')),
        'versions':{'python':platform.python_version(),'torch':torch.__version__,'transformers':transformers.__version__},
        'hardware':{'gpu':torch.cuda.get_device_name(0),'cuda':torch.version.cuda,'mixed_precision':str(amp_dtype)},
        'parameters':sum(p.numel()for p in model.parameters()),'tokenization':stats,'history':[]}
    best=-1
    for epoch in range(1,CONFIG['epochs']+1):
        model.train();optimizer.zero_grad(set_to_none=True);train_loss=0;n=0;epoch_start=time.perf_counter()
        for step,batch in enumerate(train_loader):
            batch={k:v.to(device,non_blocking=True)for k,v in batch.items()}
            # Weight microbatches by actual example count, including final incomplete group.
            group_start=(step//CONFIG['gradient_accumulation'])*CONFIG['gradient_accumulation']
            examples_in_group=min(CONFIG['gradient_accumulation']*CONFIG['batch_size'],
                                  len(datasets['train'])-group_start*CONFIG['batch_size'])
            with torch.autocast('cuda',dtype=amp_dtype):
                output=model(**batch)
                loss=output.loss*len(batch['labels'])/examples_in_group
            scaler.scale(loss).backward()
            train_loss+=float(output.loss.detach())*len(batch['labels']);n+=len(batch['labels'])
            if (step+1)%CONFIG['gradient_accumulation']==0 or step+1==len(train_loader):
                scaler.unscale_(optimizer)
                torch.nn.utils.clip_grad_norm_(model.parameters(),CONFIG['max_grad_norm'])
                scaler.step(optimizer);scaler.update();scheduler.step();optimizer.zero_grad(set_to_none=True)
            if smoke:
                print('SMOKE PASS: pretrained BERT forward/backward; GPU peak MB',torch.cuda.max_memory_allocated()/2**20,flush=True)
                return
            if (step+1)%100==0:
                print(f'epoch {epoch}/3 batch {step+1}/{len(train_loader)} loss={train_loss/n:.4f} elapsed={time.perf_counter()-epoch_start:.0f}s',flush=True)
        pred,prob,vloss=infer(loaders['valid'])
        metric=scores(frames['valid'].label,pred)
        record={'epoch':epoch,'train_loss':train_loss/n,'validation_loss':vloss,**metric,
                'seconds':time.perf_counter()-epoch_start}
        result['history'].append(record)
        print('VALIDATION',record,flush=True)
        if metric['macro_f1']>best:
            best=metric['macro_f1'];result['selected_epoch']=epoch
            model.save_pretrained(OUT/'best_model',safe_serialization=True)
            tokenizer.save_pretrained(OUT/'best_model')
        save_json(OUT/'training_progress.json',result)
    del model,optimizer,scheduler
    gc.collect();torch.cuda.empty_cache()
    model=BertForSequenceClassification.from_pretrained(OUT/'best_model',local_files_only=True,
        attn_implementation='sdpa').to(device)
    pred,prob,test_loss=infer(loaders['test'])
    result['test']={**evaluate(frames['test'],pred,prob,OUT,'bert'),'loss':test_loss}
    result['seconds']=time.perf_counter()-started
    result['peak_gpu_memory_mb']=torch.cuda.max_memory_allocated()/2**20
    save_json(OUT/'results.json',result)
    print('T3 COMPLETE',result['test']['accuracy'],result['test']['macro_f1'],'epoch',result['selected_epoch'],flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--smoke',action='store_true')
    parser.add_argument('--batch-size',type=int,default=4)
    parser.add_argument('--gradient-accumulation',type=int,default=8)
    parser.add_argument('--eval-batch-size',type=int,default=8)
    args=parser.parse_args()
    assert args.batch_size>0 and args.gradient_accumulation>0 and args.eval_batch_size>0
    CONFIG.update(batch_size=args.batch_size,gradient_accumulation=args.gradient_accumulation,eval_batch_size=args.eval_batch_size)
    main(args.smoke)
