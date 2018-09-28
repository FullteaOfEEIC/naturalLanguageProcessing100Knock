from knock30 import neko

for i in range(1, len(neko) - 1):
    if neko[i]["surface"] == "の" and neko[i - 1]["pos"] == "名詞" and neko[i + 1]["pos"] == "名詞":
        print("{0}の{1}".format(neko[i - 1]["surface"], neko[i + 1]["surface"]))
