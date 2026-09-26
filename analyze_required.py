"""Recompute every score from per-document predictions and build fixed-split analyses."""
import json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import binomtest
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix,classification_report
from nlp_common import ROOT,CLASSES,load_splits,scores,save_json,provenance
OUT=ROOT/'required_analysis';OUT.mkdir(exist_ok=True)
def read(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
f=load_splits()['test'];ids=f.row_id.to_numpy();y=f.label.to_numpy();pred={};meta={}
t1=read('t1_results/results.json');tab=pd.read_csv(ROOT/'t1_results/test_predictions.csv').set_index('row_id').loc[ids]
for n,k in [('Binary','binary'),('Count','count')]:
    pred[n]=tab[k].to_numpy();m=t1['models'][k]
    meta[n]={'test':{key:m[key] for key in ['accuracy','macro_f1','report','confusion']},'C':m['C'],
             'validation':max((x for x in t1['validation'] if x['model']==k),key=lambda x:(x['macro_f1'],-x['C']))}
specs=[('TF-IDF','t1_tfidf_results/tfidf_predictions.csv','t1_tfidf_results/results.json',None),
       *[(n,f't2_required_results/{k}_raw_mean_predictions.csv',f't2_required_results/{k}_results.json','raw_mean')for n,k in [('GloVe','glove'),('AG-W2V','ag'),('NYT-W2V','nyt')]],
       ('BERT-64','t3_64_results/bert_predictions.csv','t3_64_results/results.json',None),
       ('Count-head64','bow_head64_results/head64_predictions.csv','bow_head64_results/results.json',None),
       ('BERT-512','t3_results/bert_predictions.csv','t3_results/results.json',None)]
for n,p,r,variant in specs:
    data=pd.read_csv(ROOT/p).set_index('row_id').loc[ids];assert data.label.tolist()==f.label.tolist()
    pred[n]=data.prediction.to_numpy();result=read(r);assert result['provenance']==provenance()
    m=result['models'][variant] if variant else result
    meta[n]={'test':m['test'],'C':m.get('C'),'validation':m.get('selected_validation')}
    if 'history'in m:meta[n]['validation']=next(x for x in m['history'] if x['epoch']==m['selected_epoch'])
for n,p in pred.items():
    recomputed=scores(y,p)
    for metric,value in recomputed.items():assert abs(value-meta[n]['test'][metric])<1e-12,(n,metric)
    cm=confusion_matrix(y,p,labels=CLASSES);assert cm.tolist()==meta[n]['test']['confusion']
    meta[n]['errors']=int((y!=p).sum())
allp=f[['row_id','label']].copy()
for n,p in pred.items():allp[n]=p
allp.to_csv(OUT/'all_predictions.csv',index=False)
rng=np.random.default_rng(42);samples=rng.integers(0,len(y),size=(3000,len(y)))
yi=np.array([CLASSES.index(a)for a in y]);pi={n:np.array([CLASSES.index(a)for a in p])for n,p in pred.items()}
def fast_f1(a,b):
    cm=np.bincount(3*a+b,minlength=9).reshape(3,3)
    return np.mean(np.divide(2*np.diag(cm),cm.sum(0)+cm.sum(1),out=np.zeros(3),where=(cm.sum(0)+cm.sum(1))!=0))
pairs={}
for a,b in [('Binary','Count'),('Count','TF-IDF'),('AG-W2V','NYT-W2V'),('GloVe','NYT-W2V'),('Count','BERT-64'),('Count-head64','BERT-64'),('BERT-64','BERT-512')]:
    wrong_a=pred[a]!=y;wrong_b=pred[b]!=y
    fixes=int((wrong_a&~wrong_b).sum());adds=int((~wrong_a&wrong_b).sum())
    diffs=[fast_f1(yi[ix],pi[b][ix])-fast_f1(yi[ix],pi[a][ix])for ix in samples]
    pairs[a+' -> '+b]={'fixes':fixes,'adds':adds,'common_errors':int((wrong_a&wrong_b).sum()),
        'macro_f1_delta':meta[b]['test']['macro_f1']-meta[a]['test']['macro_f1'],
        'macro_f1_ci95':np.quantile(diffs,[.025,.975]).tolist(),
        'mcnemar_exact_p':float(binomtest(min(fixes,adds),fixes+adds,.5).pvalue) if fixes+adds else 1.0}
analyzer=CountVectorizer().build_analyzer();lengths=f.text.map(lambda t:len(analyzer(t))).to_numpy()
buckets=[]
for lo,hi in [(0,200),(200,500),(500,1000),(1000,1000000)]:
    mask=(lengths>=lo)&(lengths<hi)
    buckets.append({'lo':lo,'hi':hi,'n':int(mask.sum()),'counts':f.loc[mask,'label'].value_counts().to_dict(),
                    'models':{n:{'errors':int((p[mask]!=y[mask]).sum()),**scores(y[mask],p[mask])}for n,p in pred.items()}})
coverage_analysis={}
for source in ['glove','ag','nyt']:
    cov=pd.read_csv(ROOT/f't2_required_results/{source}_test_coverage.csv').set_index('row_id').loc[ids]
    n={'glove':'GloVe','ag':'AG-W2V','nyt':'NYT-W2V'}[source]
    coverage_analysis[n]={}
    for tag,mask in [('below98',cov.coverage.to_numpy()<.98),('atleast98',cov.coverage.to_numpy()>=.98)]:
        coverage_analysis[n][tag]={'n':int(mask.sum()),'errors':int((pred[n][mask]!=y[mask]).sum()),
                                  'accuracy':float((pred[n][mask]==y[mask]).mean()) if mask.any() else None}
save_json(OUT/'analysis.json',{'models':meta,'pairs':pairs,'length_buckets':buckets,'coverage':coverage_analysis})
primary=['Binary','Count','GloVe','AG-W2V','NYT-W2V','BERT-64']
fig,axes=plt.subplots(2,3,figsize=(10,6))
for ax,n in zip(axes.flat,primary):
    cm=np.array(meta[n]['test']['confusion']);ax.imshow(cm,cmap='Blues')
    for i in range(3):
        for j in range(3):ax.text(j,i,str(cm[i,j]),ha='center',va='center',color='white'if cm[i,j]>430 else 'black',fontsize=10)
    ax.set(xticks=range(3),yticks=range(3),xticklabels=CLASSES,yticklabels=CLASSES,title=n,xlabel='Predicted',ylabel='True')
fig.tight_layout();fig.savefig(OUT/'required_confusions.png',dpi=200);plt.close(fig)
fig,axes=plt.subplots(1,2,figsize=(10,3.5))
for ax,key,title in zip(axes,['accuracy','macro_f1'],['Test Accuracy (%)','Test Macro-F1 (%)']):
    vals=[100*meta[n]['test'][key]for n in primary];bars=ax.barh(primary,vals,color=['#71899b','#257c99','#4c8c75','#7aa58a','#bd9853','#986878'])
    ax.set_xlim(0,105);ax.set_title(title);ax.invert_yaxis()
    for bar,v in zip(bars,vals):ax.text(v+.4,bar.get_y()+bar.get_height()/2,f'{v:.2f}',va='center',fontsize=8)
fig.tight_layout();fig.savefig(OUT/'required_metrics.png',dpi=200);plt.close(fig)
b=read('t3_64_results/results.json');fig,ax=plt.subplots(figsize=(7,3))
ax.plot([1,2,3],[x['train_loss']for x in b['history']],'o-',label='Training loss')
ax.plot([1,2,3],[x['validation_loss']for x in b['history']],'s-',label='Validation loss')
ax.set(xlabel='Epoch',ylabel='Cross-entropy loss',xticks=[1,2,3]);ax.legend();fig.tight_layout();fig.savefig(OUT/'bert64_training.png',dpi=200);plt.close(fig)
print(json.dumps({'pairs':pairs,'length':buckets,'coverage':coverage_analysis},ensure_ascii=False,indent=2))
