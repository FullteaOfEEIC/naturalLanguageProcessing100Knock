import sys

N = int(sys.argv[1])
with open("hightemp.txt", "r") as fp:
    for line in fp:
        print("\t".join(line.split("\t")[:N:]))
