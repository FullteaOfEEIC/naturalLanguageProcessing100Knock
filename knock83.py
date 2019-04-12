from knock82 import db
import numpy as np
from tqdm import tqdm
import json
import plyvel

word2num={}
num2word={}

for i,data in tqdm(enumerate(db)):
    word=data[0].decode("utf-8")
    word2num[word]=i
    num2word[i]=word

f=plyvel.DB("./knock83.ldb".format(word), create_if_missing=True)

if __name__=="__main__":
    size=len(num2word)
    for i in tqdm(range(size)):
        word=num2word[i]
        data=json.loads(db.get(word.encode("utf-8")))
        row=np.zeros(size,dtype=np.uint8)
        row[i]=data["count"]
        c=data["c"]
        for _c in c:
            row[word2num[str(_c)]]=c[_c]
        f.put(word.encode("utf-8"),row)
