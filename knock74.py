from knock73 import model
from knock72 import word2num, num2word, stemmer
import sys


vector = [0 for i in range(len(word2num))]
scentence = sys.argv[1::]
for word in scentence:
        word = stemmer.stemWord(word)
        if word in word2num:
            vector[word2num[word]] = 1

print("score:", model.predict([vector]))
print("probability:", model.predict_proba([vector]))
