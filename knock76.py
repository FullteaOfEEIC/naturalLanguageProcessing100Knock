from knock72 import remove_stopwords
from knock73 import model
from knock74 import createVec
import numpy as np
import re

def label():
    retval=[]
    with open("./sentiment.txt", "r") as fp:
        for line in fp:
            score = int(line[:2:])
            line = re.sub("[\[\]]", "", line[3::])
            line = remove_stopwords(line)
            vector=createVec(line)
            predict=model.predict([vector])
            probability=np.max(model.predict_proba([vector]))
            retval.append((score,predict[0],probability))
    return retval

if __name__=="__main__":
    for i in label():
        print("{0}\t{1}\t{2}".format(i[0],i[1],i[2]))
