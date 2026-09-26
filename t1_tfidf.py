"""Supplementary third BoW representation: TF-IDF. Not an explicitly named requirement."""
import warnings, joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.exceptions import ConvergenceWarning
from nlp_common import ROOT,load_splits,provenance,scores,evaluate,save_json
warnings.filterwarnings('error',category=ConvergenceWarning)
f=load_splits();out=ROOT/'t1_tfidf_results';out.mkdir(exist_ok=True)
v=TfidfVectorizer(lowercase=True,min_df=1,token_pattern=r'(?u)\b\w\w+\b',norm='l2',smooth_idf=True,sublinear_tf=False)
x={'train':v.fit_transform(f['train'].text)}
for s in ['valid','test']:x[s]=v.transform(f[s].text)
trials=[];clfs=[]
for c in [.01,.1,1,10,100,1000]:
    clf=OneVsRestClassifier(LogisticRegression(C=c,solver='liblinear',max_iter=5000,random_state=42)).fit(x['train'],f['train'].label)
    trials.append({'C':c,**scores(f['valid'].label,clf.predict(x['valid']))});clfs.append(clf)
i=max(range(len(trials)),key=lambda i:(trials[i]['macro_f1'],-trials[i]['C']));clf=clfs[i]
r={'provenance':provenance(),'vocabulary':len(v.vocabulary_),'C':trials[i]['C'],'validation':trials,
   'selected_validation':trials[i],'test':evaluate(f['test'],clf.predict(x['test']),clf.predict_proba(x['test']),out,'tfidf')}
save_json(out/'results.json',r);joblib.dump((v,clf),out/'model.joblib');print(r['C'],r['test']['accuracy'],r['test']['macro_f1'])
