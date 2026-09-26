"""Required T2: GloVe 6B 100d, AG Skip-gram, NYT-train Skip-gram. Raw mean is primary.
Run --models ag nyt; after prepare_glove.py run --models glove.
L2-normalized mean is a separately identified ablation; never select it using test.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','4')
import argparse, time, re, zlib, hashlib, platform, warnings, json
from pathlib import Path
import numpy as np
import pandas as pd
import gensim, sklearn, joblib
from gensim.models import Word2Vec, KeyedVectors
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import ConvergenceWarning
from nlp_common import ROOT, CLASSES, load_splits, provenance, scores, evaluate, save_json
warnings.filterwarnings('error',category=ConvergenceWarning)
OUT=ROOT/'t2_required_results';OUT.mkdir(exist_ok=True)
GRID=[.01,.1,1,10,100,1000]
def stable_hash(s): return zlib.crc32(s.encode('utf-8'))
def main(names):
    frames=load_splits();analyzer=CountVectorizer().build_analyzer()
    tokens={n:[analyzer(s) for s in f.text] for n,f in frames.items()}
    cfg=dict(vector_size=100,sg=1,window=5,min_count=2,negative=5,hs=0,sample=.001,epochs=10,workers=1,seed=42)
    for name in names:
        began=time.perf_counter();info={}
        if name=='ag':
            raw=pd.read_csv(ROOT/'ag.csv'); assert raw.text.notna().all()
            clean=raw.drop_duplicates('text');nyt_texts=set(pd.read_csv(ROOT/'nyt.csv').text)
            overlap=clean.text.isin(nyt_texts);clean=clean.loc[~overlap]
            sentences=[analyzer(s) for t in clean.text for s in re.split(r'[.!?]+',t)]
            sentences=[s for s in sentences if s]
            info={'source':'ag.csv','sha256':hashlib.sha256((ROOT/'ag.csv').read_bytes()).hexdigest(),
                  'raw_documents':len(raw),'duplicate_documents':len(raw)-len(raw.drop_duplicates('text')),
                  'exact_overlap_with_nyt_removed':int(overlap.sum()),'documents':len(clean),
                  'sentences':len(sentences),'tokens':sum(map(len,sentences)),'training':cfg}
            print('AG training',info,flush=True)
            model=Word2Vec(sentences=sentences,hashfxn=stable_hash,**cfg)
            kv=model.wv;kv.save(str(OUT/'ag.kv'));del model,sentences
        elif name=='nyt':
            # Exactly the existing seed-42 Skip-gram run; no NYT validation/test embedding training.
            kv=KeyedVectors.load(str(ROOT/'t2_results'/'skipgram.kv'))
            info={'source':'NYT training partition only; reuse verified t2_experiment.py Skip-gram vectors',
                  'documents':len(frames['train']),'training':cfg,
                  'embedding_sha256':hashlib.sha256((ROOT/'t2_results'/'skipgram.kv').read_bytes()).hexdigest()}
        else:
            src=ROOT/'models'/'glove'/'glove.6B.100d.txt'
            info=json.loads(src.with_name('source.json').read_text())
            # Load the complete public vocabulary; no dataset-driven embedding fitting.
            kv=KeyedVectors.load_word2vec_format(str(src),binary=False,no_header=True)
        assert kv.vector_size==100
        arrays={};coverage={}
        for split,docs in tokens.items():
            x=np.zeros((len(docs),100),dtype=np.float32);known=total=empty=0;rows=[]
            for i,doc in enumerate(docs):
                keep=[w for w in doc if w in kv];total+=len(doc);known+=len(keep)
                if keep:x[i]=kv[keep].mean(axis=0)
                else:empty+=1
                rows.append({'row_id':int(frames[split].row_id.iloc[i]),'label':frames[split].label.iloc[i],
                             'tokens':len(doc),'known':len(keep),'coverage':len(keep)/max(1,len(doc))})
            arrays[split]=x
            coverage[split]={'known':known,'total':total,'token_coverage':known/total,'empty_vectors':empty}
            pd.DataFrame(rows).to_csv(OUT/f'{name}_{split}_coverage.csv',index=False)
        np.savez_compressed(OUT/f'{name}_mean_vectors.npz',**arrays)
        result={'provenance':provenance(),'source':info,'vocabulary':len(kv),'vector_size':100,
                'coverage':coverage,'C_grid':GRID,'primary':'raw_mean',
                'versions':{'python':platform.python_version(),'gensim':gensim.__version__,'sklearn':sklearn.__version__},
                'neighbors':{w:kv.most_similar(w,topn=5) for w in ['market','government','football'] if w in kv},'models':{}}
        for variant in ['raw_mean','l2_mean']:
            xs=arrays if variant=='raw_mean' else {s:normalize(a) for s,a in arrays.items()}
            trials=[];clfs=[]
            for c in GRID:
                clf=OneVsRestClassifier(LogisticRegression(C=c,solver='liblinear',max_iter=5000,random_state=42))
                clf.fit(xs['train'],frames['train'].label)
                trials.append({'C':c,**scores(frames['valid'].label,clf.predict(xs['valid']))});clfs.append(clf)
            ix=max(range(len(trials)),key=lambda i:(trials[i]['macro_f1'],-trials[i]['C']))
            clf=clfs[ix];assert clf.classes_.tolist()==CLASSES
            tag=name+'_'+variant
            joblib.dump(clf,OUT/f'{tag}_classifier.joblib')
            test=evaluate(frames['test'],clf.predict(xs['test']),clf.predict_proba(xs['test']),OUT,tag)
            result['models'][variant]={'C':trials[ix]['C'],'validation':trials,'selected_validation':trials[ix],'test':test}
            print(tag,'C',trials[ix]['C'],'TEST',test['accuracy'],test['macro_f1'],flush=True)
        result['seconds']=time.perf_counter()-began
        save_json(OUT/f'{name}_results.json',result)
        del kv,arrays
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--models',nargs='+',choices=['ag','nyt','glove'],default=['ag','nyt','glove'])
    main(p.parse_args().models)
