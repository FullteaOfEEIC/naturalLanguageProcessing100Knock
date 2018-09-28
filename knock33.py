from knock30 import neko

for nya in neko:
    if nya["pos"] == "名詞" and nya["pos1"] == "サ変接続":
        print(nya["surface"])
