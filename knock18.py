with open("hightemp.txt", "r") as fp:
    fd = fp.readlines()
    fd.sort(key=lambda x: x.split("\t")[2], reverse=True)
    for txt in fd:
        print(txt)
