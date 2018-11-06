from knock50 import scentences
import re

marks=re.compile("[.;:?!,]")

for scentence in scentences:
    for i in scentence.split(" "):
        word=re.sub(marks,"",i)
        print(word)
    print("")
