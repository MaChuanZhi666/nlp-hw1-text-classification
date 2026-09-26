"""Shared data contract and evaluation for T2/T3; never create new splits."""
from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix

ROOT = Path(__file__).resolve().parent
CLASSES = ['business', 'politics', 'sports']

def load_splits():
    raw = pd.read_csv(ROOT / 'nyt.csv').assign(row_id=lambda x: np.arange(len(x)))
    manifest = pd.read_csv(ROOT / 't1_results' / 'splits.csv')
    assert manifest.row_id.is_unique and len(manifest) == len(raw.drop_duplicates('text'))
    frames = {}
    for name in ['train', 'valid', 'test']:
        ids = manifest.loc[manifest.split.eq(name), 'row_id'].to_numpy()
        frame = raw.iloc[ids].copy().reset_index(drop=True)
        assert frame.label.tolist() == manifest.loc[manifest.split.eq(name),'label'].tolist()
        frames[name] = frame
    assert all(not (set(frames[a].text) & set(frames[b].text)) for a,b in [('train','valid'),('train','test'),('valid','test')])
    return frames

def provenance():
    return {name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['nyt.csv','t1_results/splits.csv']}

def scores(y, pred):
    return {'accuracy':float(accuracy_score(y,pred)),
            'macro_f1':float(f1_score(y,pred,labels=CLASSES,average='macro',zero_division=0))}

def evaluate(frame, pred, prob, out, name):
    out = Path(out); out.mkdir(exist_ok=True,parents=True)
    p = frame[['row_id','label','text']].copy()
    p['prediction'] = pred
    p['confidence'] = np.max(prob,axis=1)
    for k,c in enumerate(CLASSES): p['prob_'+c] = prob[:,k]
    p.to_csv(out/f'{name}_predictions.csv',index=False)
    cm = confusion_matrix(frame.label,pred,labels=CLASSES)
    pd.DataFrame(cm,index=CLASSES,columns=CLASSES).to_csv(out/f'{name}_confusion.csv')
    p.loc[p.label.ne(p.prediction)].to_csv(out/f'{name}_errors.csv',index=False)
    return {**scores(frame.label,pred),'report':classification_report(frame.label,pred,labels=CLASSES,output_dict=True,zero_division=0),
            'confusion':cm.tolist(),'errors':int(p.label.ne(p.prediction).sum())}

def save_json(path, data):
    Path(path).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
