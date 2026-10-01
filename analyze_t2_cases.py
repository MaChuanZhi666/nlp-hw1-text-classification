"""Audit three source-disagreement cases without fitting or selecting any model."""
from collections import Counter
import json
import joblib
import numpy as np
import pandas as pd
from gensim.models import KeyedVectors
from sklearn.feature_extraction.text import CountVectorizer
from nlp_common import ROOT, load_splits, save_json

IDS=[2849,9704,11327]
frame=load_splits()['test'].set_index('row_id')
analyzer=CountVectorizer().build_analyzer()
cases={str(i):{'row_id':i,'label':frame.loc[i,'label'],'text':frame.loc[i,'text'],'sources':{}} for i in IDS}
for source in ['glove','ag','nyt']:
    kv=(KeyedVectors.load_word2vec_format(str(ROOT/'models/glove/glove.6B.100d.txt'),no_header=True)
        if source=='glove' else KeyedVectors.load(str(ROOT/('t2_required_results/ag.kv' if source=='ag' else 't2_results/skipgram.kv'))))
    clf=joblib.load(ROOT/f't2_required_results/{source}_raw_mean_classifier.joblib')
    saved=pd.read_csv(ROOT/f't2_required_results/{source}_raw_mean_predictions.csv').set_index('row_id')
    coverage=pd.read_csv(ROOT/f't2_required_results/{source}_test_coverage.csv').set_index('row_id')
    for i in IDS:
        c=cases[str(i)];tokens=analyzer(c['text']);known=[w for w in tokens if w in kv]
        x=kv[known].mean(axis=0).reshape(1,-1);scores=clf.decision_function(x)[0]
        prediction=clf.predict(x)[0];assert prediction==saved.loc[i,'prediction']
        assert len(known)==coverage.loc[i,'known']
        # Fixed semantic contrast per document, also for the correctly classified sources.
        other={2849:'business',9704:'sports',11327:'sports'}[i]
        ia=list(clf.classes_).index(other);ib=list(clf.classes_).index(c['label'])
        wa=clf.estimators_[ia].coef_[0]-clf.estimators_[ib].coef_[0]
        intercept=float(clf.estimators_[ia].intercept_[0]-clf.estimators_[ib].intercept_[0])
        terms=[{'token':w,'count':n,'contribution':float(n*np.dot(kv[w],wa)/len(known))} for w,n in Counter(known).items()]
        margin=float(scores[ia]-scores[ib]);assert abs(intercept+sum(t['contribution'] for t in terms)-margin)<1e-4
        terms.sort(key=lambda t:t['contribution'],reverse=True)
        c['sources'][source]={'prediction':prediction,'coverage':len(known)/len(tokens),'known':len(known),'total':len(tokens),
          'oov':dict(Counter(w for w in tokens if w not in kv)),'contrast':other+' minus '+c['label'],
          'margin':margin,'intercept':intercept,'terms':terms,'probabilities':dict(zip(clf.classes_,map(float,clf.predict_proba(x)[0])))}
    del kv
save_json(ROOT/'required_analysis/t2_case_evidence.json',{'selection':'Post-hoc illustrative cases: AG-only, NYT-only and GloVe-only errors; not a random sample.','cases':cases})
for i,c in cases.items():
    print(i,c['label'])
    for s,v in c['sources'].items():
        print(s,v['prediction'],'coverage',round(v['coverage']*100,2),'margin',round(v['margin'],3),'oov',v['oov'])
        print('positive',[(t['token'],round(t['contribution'],3)) for t in v['terms'][:5]],'negative',[(t['token'],round(t['contribution'],3)) for t in v['terms'][-5:]])
