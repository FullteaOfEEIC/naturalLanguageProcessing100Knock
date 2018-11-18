from knock51 import words
import snowballstemmer

stemmer=snowballstemmer.stemmer("english")
for word in words:
    if word!="":
        print("{0}\t{1}".format(word,stemmer.stemWord(word)))
    else:
        print("")
