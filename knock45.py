from knock41 import neko


# なんて汚いコード...!!
for scentence in neko:
    for chunk in scentence:
        for morph in chunk.morphs:
            if (morph.pos or morph.pos1) == "動詞":
                left = morph.base
                right = []
                for i in chunk.srcs:
                    ch = scentence[i]
                    for mp in ch.morphs:
                        if (mp.pos or mp.pos1) == "助詞":
                            right.append(mp.base)
                if len(left) > 0:
                    print("{0}\t{1}".format(left, " ".join(right)))
