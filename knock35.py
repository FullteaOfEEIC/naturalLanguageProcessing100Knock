from knock30 import neko

noun=""
for nya in neko:
    if nya["pos"]=="名詞":
        noun+=nya["surface"]
    elif noun!="":
        print(noun)
        noun=""

if noun!="":
    print(noun)
