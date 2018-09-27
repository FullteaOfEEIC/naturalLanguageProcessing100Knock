import json
import sys


def uk():
    with open("jawiki-country.json", "r") as fp:
        for line in fp:
            dictionary = json.loads(line)
            if dictionary["title"] == "イギリス":
                return dictionary["text"]


if __name__ == "__main__":
    print(uk())
