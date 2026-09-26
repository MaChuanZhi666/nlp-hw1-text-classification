"""Download an official BERT snapshot into the workspace (no training data uploaded)."""
import os
from pathlib import Path
os.environ['HF_HUB_DISABLE_XET']='1'
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING']='1'
from huggingface_hub import HfApi, snapshot_download
from nlp_common import ROOT, save_json

if __name__=='__main__':
    repo='google-bert/bert-base-uncased'
    # Pin the exact snapshot used in the completed homework experiments.
    info=HfApi().model_info(repo,revision='86b5e0934494bd15c9632b12f734a8a67f723594')
    dest=ROOT/'models'/'bert-base-uncased'
    print('Downloading',repo,'revision',info.sha,flush=True)
    snapshot_download(repo_id=repo,revision=info.sha,local_dir=dest,
        allow_patterns=['config.json','model.safetensors','tokenizer.json','tokenizer_config.json','vocab.txt'],max_workers=2)
    save_json(dest/'source.json',{'repo_id':repo,'revision':info.sha,'url':'https://huggingface.co/'+repo})
    print('BERT download complete',flush=True)
