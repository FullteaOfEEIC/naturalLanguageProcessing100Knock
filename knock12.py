with open("hightemp.txt", "r") as fp:
    content = [i.split("\t") for i in fp.readlines()]
with open("col1.txt", "w") as col1:
    col1.writelines([i[0] + "\n" for i in content])

with open("col2.txt", "w") as col2:
    col2.writelines([i[1] + "\n" for i in content])
