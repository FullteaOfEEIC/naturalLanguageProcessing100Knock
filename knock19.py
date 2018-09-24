with open("hightemp.txt", "r") as fp:
    dictionary = {}
    for line in fp:
        pref = line.split("\t")[0]
        dictionary[pref] = dictionary.get(pref, 0) + 1

result = list(dictionary.items())
result.sort(key=lambda x: x[1], reverse=True)
for pref in result:
    print(pref[0])
