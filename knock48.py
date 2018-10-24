from knock41 import neko
from knock47 import index


def tree(scentence, i):
    dst = i
    path = []
    while dst != -1:
        chunk = scentence[dst]
        path.append(chunk)
        dst = chunk.dst
    return path


if __name__ == "__main__":
    for scentence in neko:
        for i in range(len(scentence)):
            if index(scentence[i], "名詞") != []:
                result = tree(scentence, i)
                if len(result) > 1:
                    print(" -> ".join([i.surface for i in result]))
