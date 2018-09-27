from knock20 import uk
import re

def template():
    rec=False
    result={}
    info=re.compile("\|(.*) = (.*)")
    for text in uk().split("\n"):
        if rec:
            m=info.search(text)
            if m:
                result[m.group(1)]=m.group(2)

        elif "基礎情報" in text:
            rec=True
        elif text=="\}\}":
            rec=False
    return result

if __name__=="__main__":
    print(template())
