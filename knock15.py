import sys

N = int(sys.argv[1])
with open("hightemp.txt", "r") as fp:
    for line in fp:
        l = line.split("\t")
        print("\t".join(l[len(l) - N::]))
