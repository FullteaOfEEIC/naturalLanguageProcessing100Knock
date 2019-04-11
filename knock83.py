from knock82 import db
import numpy as np
from tqdm import tqdm
import json

word2num={}
num2word={}

for i,data in tqdm(enumerate(db)):
    word=data[0].decode("utf-8")
    word2num[word]=i
    num2word[i]=word


for i in range(len(num2word)):
    word=num2word[i]
    print(word,json.loads(db.get(word.encode("utf-8"))))
    print()
    print()
