from knock30 import neko

count = {}
for nya in neko:
    count[nya["base"]] = count.get(nya["base"], 0) + 1

del count[None]
count = sorted(count.items(), key=lambda x: -x[1])
if __name__=="__main__":
    for c in count:
        print(c[0])
        
