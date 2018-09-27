from knock26 import template26
import re


def template27():
    tmp = template26()
    linkMarkUp = re.compile(r"\[\[(.*?)((#.*)?\|.*)?]]")
    for key in tmp:
        m = linkMarkUp.search(tmp[key])
        if m:
            tmp[key] = linkMarkUp.sub(m.group(1), tmp[key])

    return tmp


if __name__ == "__main__":
    tmp = template27()
    for key in tmp:
        print("|{0} = {1}".format(key, tmp[key]))
