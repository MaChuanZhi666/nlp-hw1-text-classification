"""Train CBOW/Skip-gram on training texts only, mean pooling, L2 normalize, OvR LR.
Run with .venv/Scripts/python.exe t2_experiment.py
"""
import os
os.environ.setdefault('OMP_NUM_THREADS','4')
from pathlib import Path
import time
import re
import zlib
import warnings
import platform
import numpy as np
import gensim
import sklearn
import joblib
from gensim.models import Word2Vec
from gensim.models.callbacks import CallbackAny2Vec
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import ConvergenceWarning
from nlp_common import ROOT, CLASSES, load_splits, provenance, scores, evaluate, save_json

warnings.filterwarnings('error', category=ConvergenceWarning)
OUT=ROOT/'t2_results'; OUT.mkdir(exist_ok=True)

def stable_hash(value):
    return zlib.crc32(value.encode('utf-8'))

class Progress(CallbackAny2Vec):
    def __init__(self,name): self.name=name; self.epoch=0; self.start=time.perf_counter()
    def on_epoch_end(self, model):
        self.epoch+=1
        print(f'{self.name} embedding epoch {self.epoch}/10 elapsed {time.perf_counter()-self.start:.1f}s',flush=True)

def main():
    start=time.perf_counter()
    frames=load_splits()
    analyzer=CountVectorizer().build_analyzer()
    tokens={n:[analyzer(s) for s in f.text] for n,f in frames.items()}
    # Sentence boundaries constrain context windows; no validation/test text in vocabulary/training.
    sentences=[analyzer(s) for text in frames['train'].text for s in re.split(r'[.!?]+',text)]
    sentences=[s for s in sentences if s]
    result={'provenance':provenance(),'classes':CLASSES,'seed':42,
        'versions':{'python':platform.python_version(),'gensim':gensim.__version__,'sklearn':sklearn.__version__},
        'config':{'vector_size':100,'window':5,'min_count':2,'negative':5,'sample':.001,'epochs':10,'workers':1,
                  'pooling':'mean of in-vocabulary tokens, including repeated occurrences; then L2 normalize',
                  'classifier':'OneVsRest LogisticRegression liblinear L2 class_weight=None',
                  'C_grid':[.01,.1,1,10,100],'external_corpus':False,'sentence_count':len(sentences)},
        'models':{}}
    for name,sg in [('cbow',0),('skipgram',1)]:
        began=time.perf_counter()
        embedding=Word2Vec(sentences=sentences,vector_size=100,window=5,min_count=2,sg=sg,
            negative=5,hs=0,sample=.001,epochs=10,workers=1,seed=42,hashfxn=stable_hash,callbacks=[Progress(name)])
        embedding.wv.save(str(OUT/f'{name}.kv'))
        arrays={}; coverage={}
        for split,docs in tokens.items():
            x=np.zeros((len(docs),100),dtype=np.float32)
            total=known=empty=0
            for i,doc in enumerate(docs):
                retained=[w for w in doc if w in embedding.wv]
                total+=len(doc);known+=len(retained)
                if retained: x[i]=embedding.wv[retained].mean(axis=0)
                else: empty+=1
            arrays[split]=normalize(x,norm='l2')
            coverage[split]={'token_coverage':known/total,'empty_vectors':empty}
        trials=[]; models=[]
        for c in result['config']['C_grid']:
            clf=OneVsRestClassifier(LogisticRegression(C=c,solver='liblinear',random_state=42,max_iter=2000))
            clf.fit(arrays['train'],frames['train'].label)
            metric=scores(frames['valid'].label,clf.predict(arrays['valid']))
            trials.append({'C':c,**metric});models.append(clf)
            print(name,'C',c,'validation',metric,flush=True)
        best=max(range(len(trials)),key=lambda i:(trials[i]['macro_f1'],-trials[i]['C']))
        clf=models[best]
        assert clf.classes_.tolist()==CLASSES
        joblib.dump(clf,OUT/f'{name}_classifier.joblib')
        pred=clf.predict(arrays['test']);prob=clf.predict_proba(arrays['test'])
        test=evaluate(frames['test'],pred,prob,OUT,name)
        neighbors={w:[{'word':v,'cosine':float(c)} for v,c in embedding.wv.most_similar(w,topn=6)] for w in ['company','market','insurance','government','football','team'] if w in embedding.wv}
        result['models'][name]={'sg':sg,'C':trials[best]['C'],'validation':trials,'selected_validation':trials[best],
            'test':test,'vocabulary':len(embedding.wv),'coverage':coverage,'neighbors':neighbors,'seconds':time.perf_counter()-began}
        save_json(OUT/'results.json',result)
        print('TEST',name,test['accuracy'],test['macro_f1'],flush=True)
    result['selected_model']=max(result['models'],key=lambda n:result['models'][n]['selected_validation']['macro_f1'])
    result['seconds']=time.perf_counter()-start
    save_json(OUT/'results.json',result)
    print('T2 complete. Validation-selected model:',result['selected_model'],flush=True)

if __name__=='__main__':main()
