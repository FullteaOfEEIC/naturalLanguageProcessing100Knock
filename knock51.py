from knock50 import scentences
import re

marks=re.compile("[.;:?!,]")
words=[]

for scentence in scentences:
    for i in scentence.split(" "):
        word=re.sub(marks,"",i)
        words.append(word)
    words.append("")

if __name__=="__main__":
    for word in words:
        print(word)
