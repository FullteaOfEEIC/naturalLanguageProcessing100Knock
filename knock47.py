from knock41 import neko
from knock43 import contain


for scentence in neko:
    for chunk in scentence:
        for morph in chunk.morphs:
            if (morph.pos or morph.pos1) == "動詞":
                for i in chunk.srcs:
