import sys
import math

N = int(sys.argv[1])

with open("hightemp.txt", "r") as fp:
    fd = fp.readlines()
    size = math.ceil(len(fd) / N)
    for i in range(N):
        with open("answer16-{}.txt".format(i + 1), "w") as ans:
            ans.writelines(fd[size * i:size * (i + 1):])
