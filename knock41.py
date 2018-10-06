from knock40 import Morph
import CaboCha
import  sys

def _rem(text,str):
    if str in text:
        text=text.replace(str,"")
        return _rem(text,str)
    else:
        return text

class Chunk:
    def __init__(self,parsed):
        data=parsed[0].split(" ")
        self.dst=int(data[2][:-1:])
        self.srcs=[]
        self.morphs=[]
        for p in parsed[1::]:
            self.morphs.append(Morph(p))

        
        surface="".join([i.surface for i in self.morphs])
        surface=_rem(surface,"、")
        surface=_rem(surface,"。")
        self.surface=surface

    def __repr__(self):
        return self.surface

#汚い...あまりにも...(許して)
c=CaboCha.Parser()
with open("neko.txt", "r") as fp:
    neko=[]
    for line in fp:
        if line=="":
            continue
        scentence=[]
        tree = c.parse(line)
        parsed = tree.toString(CaboCha.FORMAT_LATTICE)
        parsed=parsed.split("\n")
        parsed=parsed[:-2:]#remove EOS and ""
        if parsed==[]:
            continue
        cash=[parsed[0]]
        for p in parsed[1::]:
            if p[0]=="*":
                scentence.append(Chunk(cash))
                cash=[p]
            else:
                cash.append(p)
        scentence.append(Chunk(cash))
        for i,ch in enumerate(scentence):
            if ch.dst!=-1:
                scentence[ch.dst].srcs.append(i)
        neko.append(scentence)



if __name__=="__main__":
    print(neko[7])
    print([i.dst for i in neko[7]])
