import random

with open("./rt-polaritydata/rt-polaritydata/rt-polarity.pos","r") as fpos:
    with open("./rt-polaritydata/rt-polaritydata/rt-polarity.neg","r") as fneg:
        pos = ["+1 " + t for t in fpos.readlines()]
        neg = ["-1 " + t for t in fneg.readlines()]
        scentences = neg + pos
        random.shuffle(scentences)#MLE?よく聞こえないなぁ

with open("./sentiment.txt","w") as fp:
    fp.writelines(scentences)
