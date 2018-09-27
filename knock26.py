from knock25 import template
import re

def template26():
    tmp=template()
    strong=re.compile('"{1,3}(.*)"{1,3}')#超読みにくい
    for key in tmp:
        m=strong.search(tmp[key])
        if m:
            tmp[key]=strong.sub(m.group(1),tmp[key])

    return tmp

if __name__=="__main__":
    tmp=template26()
    for key in tmp:
        print("|{0} = {1}".format(key,tmp[key]))
