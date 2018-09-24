with open("hightemp.txt", "r") as fp:
    result = set()
    for line in fp:
        result.add(line.split("\t")[0])
print(result)
