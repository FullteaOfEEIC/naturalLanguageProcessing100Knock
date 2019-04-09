from tqdm import tqdm
import re

with open("enwiki-20150112-400-r10-105752.txt", "r") as fp_read:
    with open("corpus_tmp.txt", "w") as fp_write:
        for line in tqdm(fp_read):
            line = re.sub("\s"," ",line)
            line = re.sub("[\.\,\!\?\;\:\(\)\[\]\'\"\”\“\‘\’\—]", " ", line)
            line = re.sub(" +", " ", line)
            fp_write.write(line)
            fp_write.write("\n")
