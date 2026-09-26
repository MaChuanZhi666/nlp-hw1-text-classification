"""T1: reproducible Binary/Count Bag-of-Words + logistic regression.
Run: python t1_experiment.py
"""
from pathlib import Path
import json, warnings, platform
import numpy as np
import pandas as pd
import sklearn
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from sklearn.exceptions import ConvergenceWarning

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 't1_results'
OUT.mkdir(exist_ok=True)
warnings.filterwarnings('error', category=ConvergenceWarning)
raw = pd.read_csv(ROOT / 'nyt.csv')
assert not raw[['text', 'label']].isna().any().any()
assert not raw.text.str.strip().eq('').any()
assert raw.groupby('text').label.nunique().max() == 1
data = raw.assign(row_id=np.arange(len(raw))).drop_duplicates('text').reset_index(drop=True)
train, rest = train_test_split(data, test_size=.2, stratify=data.label, random_state=42)
valid, test = train_test_split(rest, test_size=.5, stratify=rest.label, random_state=42)
assert not (set(train.text) & set(test.text) or set(train.text) & set(valid.text) or set(valid.text) & set(test.text))
pd.concat([x[['row_id','label']].assign(split=n) for n,x in [('train',train),('valid',valid),('test',test)]]).to_csv(OUT/'splits.csv',index=False)
vectorizer = CountVectorizer(lowercase=True, min_df=1, token_pattern=r'(?u)\b\w\w+\b')
tr = vectorizer.fit_transform(train.text)
va = vectorizer.transform(valid.text)
te = vectorizer.transform(test.text)
words = vectorizer.get_feature_names_out()
classes = sorted(data.label.unique())
tokenize = vectorizer.build_analyzer()
vocab = vectorizer.vocabulary_
def metrics(y,p):
    return dict(accuracy=accuracy_score(y,p), macro_f1=f1_score(y,p,labels=classes,average='macro',zero_division=0))
result = dict(raw_n=len(raw), clean_n=len(data), duplicates=len(raw)-len(data), seed=42,
    versions=dict(python=platform.python_version(), sklearn=sklearn.__version__,pandas=pd.__version__,numpy=np.__version__),
    classes=classes, vocabulary=len(words), splits={}, models={}, validation=[])
for name, frame in [('train',train),('valid',valid),('test',test)]:
    lens=frame.text.map(lambda s:len(tokenize(s)))
    result['splits'][name]=dict(n=len(frame),counts=frame.label.value_counts().to_dict(),length=lens.describe().to_dict())
result['test_oov_rate']=sum(w not in vocab for s in test.text for w in tokenize(s))/sum(len(tokenize(s)) for s in test.text)
result['density']=tr.nnz/(tr.shape[0]*tr.shape[1])
majority=train.label.value_counts().idxmax()
result['baseline']=metrics(test.label,[majority]*len(test))
predictions=test[['row_id','label','text']].copy()
for name,binary in [('binary',True),('count',False)]:
    matrices=[x.copy() for x in [tr,va,te]]
    if binary:
        for x in matrices: x.data[:]=1
    xtrain,xvalid,xtest=matrices
    candidates=[]
    for c in [.01,.1,1.0]:
        model=OneVsRestClassifier(LogisticRegression(C=c,solver='liblinear',max_iter=2000,random_state=42))
        model.fit(xtrain,train.label)
        scores=metrics(valid.label,model.predict(xvalid))
        result['validation'].append(dict(model=name,C=c,**scores))
        candidates.append((scores['macro_f1'],c,model))
        print(name,c,scores,flush=True)
    _,c,model=max(candidates,key=lambda t:(t[0],-t[1]))
    pred=model.predict(xtest)
    prob=model.predict_proba(xtest)
    predictions[name]=pred
    predictions[name+'_confidence']=prob.max(axis=1)
    coeff=np.vstack([e.coef_[0] for e in model.estimators_])
    top={label:[dict(word=words[i],weight=float(coeff[k,i])) for i in np.argsort(coeff[k])[-15:][::-1]] for k,label in enumerate(model.classes_)}
    errors=[]
    for j in np.flatnonzero(pred!=test.label.to_numpy()):
        row=xtest.getrow(j)
        true=test.label.iloc[j]; guessed=pred[j]
        a=list(model.classes_).index(guessed); b=list(model.classes_).index(true)
        delta=row.data*(coeff[a,row.indices]-coeff[b,row.indices])
        order=np.argsort(delta)
        def evidence(ids):
            return [dict(word=words[row.indices[i]],value=int(row.data[i]),margin_contribution=float(delta[i])) for i in ids]
        errors.append(dict(row_id=int(test.row_id.iloc[j]),true=true,predicted=guessed,confidence=float(prob[j].max()),
                           text=test.text.iloc[j],toward_prediction=evidence(order[-10:][::-1]),toward_true=evidence(order[:10])))
    lengths=test.text.map(lambda s:len(tokenize(s))).to_numpy()
    bylength=[]
    for lo,hi in [(0,200),(200,500),(500,1000),(1000,1000000)]:
        mask=(lengths>=lo)&(lengths<hi)
        if mask.any(): bylength.append(dict(lo=lo,hi=hi,n=int(mask.sum()),counts=test.label.iloc[np.flatnonzero(mask)].value_counts().to_dict(),**metrics(test.label.to_numpy()[mask],pred[mask])))
    cm=confusion_matrix(test.label,pred,labels=classes)
    result['models'][name]=dict(C=c,**metrics(test.label,pred),report=classification_report(test.label,pred,output_dict=True,zero_division=0),
        confusion=cm.tolist(),top_words=top,length_buckets=bylength,errors=errors,
        max_iterations=max(int(e.n_iter_.max()) for e in model.estimators_))
    pd.DataFrame(cm,index=classes,columns=classes).to_csv(OUT/f'{name}_confusion.csv')
    fig,ax=plt.subplots(figsize=(5,4)); ax.imshow(cm,cmap='Blues')
    ax.set(xticks=range(3),yticks=range(3),xticklabels=classes,yticklabels=classes,xlabel='Predicted',ylabel='True',title=f'{name.title()} BoW + LR')
    for i in range(3):
        for j in range(3): ax.text(j,i,str(cm[i,j]),ha='center',va='center',color='white' if cm[i,j]>cm.max()/2 else 'black')
    fig.tight_layout(); fig.savefig(OUT/f'{name}_confusion.png',dpi=180);plt.close(fig)
    print('TEST',name,result['models'][name]['accuracy'],result['models'][name]['macro_f1'],flush=True)
# Paired bootstrap: uncertainty conditional on this fixed training split/models.
rng=np.random.default_rng(42)
y=test.label.to_numpy(); p=predictions.binary.to_numpy(); q=predictions['count'].to_numpy()
diff=[]
for _ in range(2000):
    ids=rng.integers(0,len(y),len(y))
    diff.append(f1_score(y[ids],p[ids],labels=classes,average='macro',zero_division=0)-f1_score(y[ids],q[ids],labels=classes,average='macro',zero_division=0))
result['paired_comparison']=dict(binary_only_correct=int(((p==y)&(q!=y)).sum()),count_only_correct=int(((q==y)&(p!=y)).sum()),both_wrong=int(((p!=y)&(q!=y)).sum()),macro_f1_difference_ci95=np.quantile(diff,[.025,.975]).tolist())
predictions.to_csv(OUT/'test_predictions.csv',index=False)
(OUT/'results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('Saved',OUT,flush=True)
