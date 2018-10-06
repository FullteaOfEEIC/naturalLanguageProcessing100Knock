import MeCab
import CaboCha
import sys

class Morph:
    def __init__(self,parsed):
        if "\t" in parsed:
            surface,analytics=parsed.split("\t")
            analytics=analytics.split(",")
            self.surface=surface
            self.base=analytics[6]
            self.pos=analytics[0]
            self.pos1=analytics[1]
        else:
            self.surface=""
            self.base=None
            self.pos=None
            self.pos1=None

    def __repr__(self):
        return self.surface


if __name__=="__main__":
    c=CaboCha.Parser()
    with open("neko.txt", "r") as fp:
        neko=[]
        for line in fp:
            tree = c.parse(line)
            parsed = tree.toString(CaboCha.FORMAT_LATTICE)
            parsed=parsed.split("\n")
            scentence=[]
            for p in parsed:
                m=Morph(p)
                scentence.append(m)
            neko.append(scentence)
        print(neko[2])
