from knock27 import template27
import re


def template28():
    tmp = template27()
    tag=re.compile(r"<.*?>")
    mark=re.compile(r"\(&.*?;\)")
    url=re.compile(r"\[https?://.*?]")
    for regex in tag,mark,url:
        for key in tmp:
            m = regex.search(tmp[key])
            if m:
                tmp[key] = regex.sub("", tmp[key])

    return tmp


if __name__ == "__main__":
    tmp = template28()
    for key in tmp:
        print("|{0} = {1}".format(key, tmp[key]))
