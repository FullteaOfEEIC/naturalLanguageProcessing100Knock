import plyvel
import random
from tqdm import tqdm
import json

db = plyvel.DB("./vector1.ldb", create_if_missing=True)


def create_db():
    retval={}
    with open("corpushead.txt", "r") as fp:
        for line in tqdm(fp):
            words = line.lower().strip().split(" ")
            len_words = len(words)
            for i, word in enumerate(words):
                tmp = retval.get(word,None)
                if tmp == None:
                    tmp = {"d": random.randint(1, 5), "c": {}}
                d = tmp["d"]
                c = tmp["c"]
                cs = words[max(0, i - d):i:] + \
                    words[i + 1:min(i + d, len_words):]
                for _c in cs:
                    c[_c] = c.get(_c, 0) + 1
                retval[word]=tmp

def save_db():
    dict=create_db()
    for key in dict:
        db.put(str(key).encode("utf-8"),json.dumps(dict[key]).encode("utf-8"))



if __name__ == "__main__":
    save_db()
    for word, value in db:
        c = json.loads(value)["c"]
        retval = [str(key) for key in c]
        print("{0}\t{1}".format(word.decode("utf-8"), ",".join(retval)))
