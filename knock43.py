from knock41 import neko

def contain(chunk,pos):
    for morph in chunk.morphs:
        if (morph.pos or morph.pos1)==pos:
            return True
    return False

for scentence in neko:
    for chunk in scentence:
        if chunk.dst!=-1:
            left=chunk
            right=scentence[chunk.dst]
            if contain(left,"名詞") and contain(right,"動詞"):
                print("{0}\t{1}".format(left,right))
