from knock41 import neko


for scentence in neko:
    for chunk in scentence:
        for morph in chunk.morphs:
            if (morph.pos or morph.pos1) == "動詞":
                left = morph.base
                center = []
                right=[]
                for i in chunk.srcs:
                    ch = scentence[i]
                    for mp in ch.morphs:
                        if (mp.pos or mp.pos1) == "助詞":
                            center.append(mp.base)
                            right.append(ch.surface)
                if len(left) > 0:
                    print("{0}\t{1}\t{2}".format(left, " ".join(center)," ".join(right)))
