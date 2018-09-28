import MeCab

m = MeCab.Tagger()
neko = []
with open("neko.txt", "r") as fp:
    for line in fp:
        parsed = m.parse(line)
        parsed = parsed.split("\n")
        for p in parsed:
            if "\t" not in p:
                continue
            surface, data = p.split("\t")
            data = data.split(",")
            word = {"surface": surface}
            word["base"] = data[6]
            word["pos"] = data[0]
            word["pos1"] = data[1]
            for key in word:
                if word[key] == "*":
                    word[key] = None
            neko.append(word)

if __name__ == "__main__":
    print(neko)
