"""Input-budget control: count BoW sees exactly BERT-64's decoded first 62 WordPieces."""
import os
os.environ.setdefault('OMP_NUM_THREADS','4')
from transformers import AutoTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.exceptions import ConvergenceWarning
import warnings, joblib
from nlp_common import ROOT,load_splits,provenance,scores,evaluate,save_json
warnings.filterwarnings('error',category=ConvergenceWarning)
f=load_splits();out=ROOT/'bow_head64_results';out.mkdir(exist_ok=True)
t=AutoTokenizer.from_pretrained(ROOT/'models'/'bert-base-uncased',local_files_only=True)
texts={}
for s,frame in f.items():
    ids=t(frame.text.tolist(),max_length=64,truncation=True,add_special_tokens=True)['input_ids']
    assert all(len(x)<=64 for x in ids)
    texts[s]=t.batch_decode(ids,skip_special_tokens=True)
v=CountVectorizer();x={'train':v.fit_transform(texts['train'])}
for s in ['valid','test']:x[s]=v.transform(texts[s])
trials=[];clfs=[]
for c in [.01,.1,1,10,100,1000]:
    clf=OneVsRestClassifier(LogisticRegression(C=c,solver='liblinear',max_iter=2000,random_state=42)).fit(x['train'],f['train'].label)
    trials.append({'C':c,**scores(f['valid'].label,clf.predict(x['valid']))});clfs.append(clf)
    print('validation',trials[-1],flush=True)
i=max(range(len(trials)),key=lambda i:(trials[i]['macro_f1'],-trials[i]['C']));clf=clfs[i]
r={'provenance':provenance(),'max_length':64,'vocabulary':len(v.vocabulary_),'C':trials[i]['C'],'validation':trials,
   'selected_validation':trials[i],'test':evaluate(f['test'],clf.predict(x['test']),clf.predict_proba(x['test']),out,'head64')}
save_json(out/'results.json',r);joblib.dump((v,clf),out/'model.joblib');print(r['C'],r['test']['accuracy'],r['test']['macro_f1'])
