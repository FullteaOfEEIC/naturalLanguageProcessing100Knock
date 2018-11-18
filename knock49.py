from knock41 import neko
from knock47 import index
from knock48 import tree


def convertNoun(chunk,letter="X"):
    retval=""
    for morph in chunk.morphs:
        if morph.pos=="名詞":
            retval+=letter
        else:
            retval+=morph.surface
    return retval


if __name__=="__main__":
    for scentence in neko:
        ind=[]
        for i,chunk in enumerate(scentence):
            if index(chunk,"名詞")!=[]:
                ind.append(i)

        for i in range(len(ind)):
            tree1=tree(scentence,i)
            for j in range(i,len(ind)):
                tree2=tree(scentence,j)
                
