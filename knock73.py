from knock72 import y, phai, word2num, num2word, stemmer
from sklearn.linear_model import LogisticRegression
import sys


model = LogisticRegression()
model.fit(phai, y)


if __name__ == "__main__":
    vector = [0 for i in range(len(word2num))]
    scentence = sys.argv[1::]
    for word in scentence:
        word=stemmer.stemWord(word)
        if word in word2num:
            vector[word2num[word]] = 1
    print(sum(vector))
    print("score:", model.predict([vector]))
    print("probability:", model.predict_proba([vector]))
