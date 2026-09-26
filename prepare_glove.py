"""Fetch the required 100d member from the official ZIP using HTTP ranges; ZIP verifies CRC."""
from pathlib import Path
import io, zipfile, requests, hashlib, json, time
ROOT=Path(__file__).resolve().parent
URL='https://downloads.cs.stanford.edu/nlp/data/glove.6B.zip'
class RemoteZip(io.RawIOBase):
    def __init__(self):
        self.pos=0; self.size=862182613
    def seekable(self): return True
    def tell(self): return self.pos
    def seek(self,offset,whence=0):
        self.pos=offset if whence==0 else self.pos+offset if whence==1 else self.size+offset
        return self.pos
    def read(self,n=-1):
        if n<0: n=self.size-self.pos
        if not n: return b''
        start=self.pos; end=min(self.size,start+n)-1
        for attempt in range(5):
            try:
                r=requests.get(URL,headers={'Range':f'bytes={start}-{end}'},stream=True,timeout=(30,90))
                r.raise_for_status()
                assert r.status_code==206 and r.headers['Content-Range'].startswith(f'bytes {start}-{end}/')
                chunks=[];total=0;last=time.monotonic()
                for b in r.iter_content(1024*1024):
                    chunks.append(b);total+=len(b)
                    if time.monotonic()-last>15:
                        print('GloVe compressed bytes',total,'/',n,flush=True);last=time.monotonic()
                data=b''.join(chunks);assert len(data)==end-start+1
                self.pos+=len(data);return data
            except Exception:
                if attempt==4: raise
                time.sleep(2)
if __name__=='__main__':
    out=ROOT/'models'/'glove';out.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(RemoteZip()) as z:
        member=z.getinfo('glove.6B.100d.txt')
        print('Downloading',member.filename,member.compress_size,flush=True)
        data=z.read(member)
        (out/member.filename).write_bytes(data)
        (out/'source.json').write_text(json.dumps({'url':URL,'member':member.filename,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'zip_crc32':member.CRC},indent=2))
        print('Verified ZIP CRC and saved',len(data),flush=True)
