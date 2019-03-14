from knock73 import model
from knock72 import word2num, num2word, stemmer, remove_stopwords
import sys


def createVec(scentence):
    vector = [0 for i in range(len(word2num))]
    scentence = remove_stopwords(scentence)
    scentence = scentence.split(" ")
    for word in scentence:
        word = stemmer.stemWord(word)
        if word in word2num:
            vector[word2num[word]] = 1
    return vector


if __name__ == "__main__":
    scentence = " ".join(sys.argv[1::])
    vector = createVec(scentence)

    print("score:", model.predict([vector]))
    print("probability:", model.predict_proba([vector]))
