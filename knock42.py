from knock41 import neko

def rem(text,str):
    if str in text:
        text=text.replace(str,"")
        return rem(text,str)
    else:
        return text

for scentence in neko:
    for chunk in scentence:
        if chunk.dst!=-1:
            left=chunk
            right=scentence[chunk.dst]
            print("{0}\t{1}".format(left,right))
