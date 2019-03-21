import plyvel
import random
from tqdm import tqdm
import json

db = plyvel.DB("./vector1.ldb", create_if_missing=True)


def create_db():
    with open("corpus.txt", "r") as fp:
        for line in tqdm(fp):
            words = line.lower().strip().split(" ")
            len_words = len(words)
            for i, word in enumerate(words):
                tmp = db.get(word.encode("utf-8"))
                if tmp == None:
                    tmp = {"d": random.randint(1, 5), "c": {}}
                else:
                    tmp = json.loads(tmp)
                d = tmp["d"]
                c = tmp["c"]
                cs = words[max(0, i - d):i:] + \
                    words[i + 1:min(i + d, len_words):]
                for _c in cs:
                    c[_c] = c.get(_c, 0) + 1
                tmp = json.dumps(tmp)
                db.put(word.encode('utf-8'), tmp.encode('utf-8'))


if __name__ == "__main__":
    create_db()
    for word, value in db:
        c = json.loads(value)["c"]
        retval = [str(key) for key in c]
        print("{0}\t{1}".format(word.decode("utf-8"), ",".join(retval)))
