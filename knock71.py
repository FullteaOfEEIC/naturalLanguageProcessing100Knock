import re
with open("./stops.txt") as fp:
    stops=[i.strip() for i in fp.readlines()]


def is_contain_stopwords(txt):
    for stop in stops:
        if re.search(" {} ".format(stop),txt) or re.search("^{} ".format(stop),txt) or re.search(" {}[.?!,]".format(stop),txt) or re.search("^{}$".format(stop),txt):
            return True
    return False


if __name__=="__main__":
    testcases=[
    "This is a pen.",
    "It always seems impossible until it’s done.",
    "Peace begins with a smile.",
    "If I were you, I wouldn't have made such a mistake.",
    "were",
    "book"
    ]
    for testcase in testcases:
        print(testcase,":",is_contain_stopwords(testcase))
