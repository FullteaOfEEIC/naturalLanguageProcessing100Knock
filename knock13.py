col1 = open("col1.txt", "r")
col2 = open("col2.txt", "r")

with open("answer13.txt", "w") as ans:
    for c1, c2 in zip(col1, col2):
        ans.write("{0}\t{1}\n".format(c1.strip(), c2.strip()))
