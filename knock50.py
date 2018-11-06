import re

separate=re.compile(r"([.;:?!]) ([A-Z])")

scentences=[]

with open("nlp.txt","r") as fp:
    for line in fp:
        _line=line.strip()
        m=re.search(separate,_line)
        while m:
            endChar=m.group(1)
            startChar=m.group(2)
            _line=_line.replace(endChar+" "+startChar,endChar+"<SEPARATE>"+startChar)
            m=re.search(separate,_line)
        _line=_line.split("<SEPARATE>")
        if _line!=[""]:
            scentences+=_line


if __name__=="__main__":
    for l in scentences:
        print(l)
