with open("hightemp.txt", "r") as fp:
    content = [txt.replace("\t", " ") for txt in fp.readlines()]

with open("answer11.txt", "w") as fp:
    fp.writelines(content)
