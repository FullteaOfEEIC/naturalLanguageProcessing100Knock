from knock41 import neko


#サ変接続名詞のMeCabによる解析は、hoge<tab>名詞,サ変接続...である(pos=名詞,pos1=サ変接続)。

def index(chunk, pos):
    result = []
    for i, morph in enumerate(chunk.morphs):
        if (morph.pos  == pos) or  (morph.pos1==pos):
            result.append(i)
    return result

def mine(scentence):
    retval=[]
    for chunk in scentence:
        _retval=[]
        joshis=[]
        nouns_ind=index(chunk,"サ変接続")
        if len(nouns_ind)>0:
            for noun_ind in nouns_ind:
                try:
                    joshi=chunk.morphs[noun_ind+1]
                except IndexError:
                    continue
                if joshi.surface=="を":
                    verbe=scentence[chunk.dst]
                    for i in verbe.srcs:
                        if (chunk==scentence[i])==False:
                            _retval.append(scentence[i])
                    retval.append((chunk,verbe,_retval))

    return retval


if __name__=="__main__":
    for scentence in neko:
        result=mine(scentence)
        for r in result:
            print("{0}{1}".format(r[0],r[1]),end="\t")
            joshis=[]
            for chunk in r[2]:
                for morph in chunk.morphs:
                    if morph.pos=="助詞":
                        joshis.append(morph.surface)
            print(" ".join(joshis),end="\t")
            print(" ".join([chunk.surface for chunk in r[2]]))
