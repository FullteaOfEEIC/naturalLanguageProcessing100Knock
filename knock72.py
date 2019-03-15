import re
import snowballstemmer
import collections

stemmer = snowballstemmer.stemmer("english")

with open("./stops.txt") as fp:
    stops = [i.strip() for i in fp.readlines()]


def remove_stopwords(text):
    retval = ""
    for t in text.split(" "):
        if t in stops + [".", ",", "--"]:
            continue
        retval += (t + " ")
    return retval.strip()


counter = collections.Counter()
file_length = 0

with open("./sentiment.txt", "r") as fp:
    for line in fp:
        score = int(line[:2:])
        line = re.sub("[\[\]]", "", line[3::])
        line = remove_stopwords(line)
        for word in line.split(" "):
            counter.update([stemmer.stemWord(word)])
        file_length += 1

wordlist = [w for w in counter if counter[w] >= 5]
word2num = {}
num2word = {}
for i, word in enumerate(wordlist):
    word2num[word] = i
    num2word[i] = word


y = []
phai = []
# ああ、頭悪い...
with open("./sentiment.txt", "r") as fp:
    for line in fp:
        score = int(line[:2:])
        line = re.sub("[\[\]]", "", line[3::])
        line = remove_stopwords(line)
        y.append(score)
        phai_i = [0 for i in range(len(word2num))]
        for word in line.split(" "):
            word = stemmer.stemWord(word)
            if word in word2num:
                phai_i[word2num[word]] = 1
        phai.append(phai_i)
