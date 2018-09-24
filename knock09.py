import random


def typoglycemia(text):
    separated = text.split(" ")
    result = []
    for word in separated:
        if len(word) > 4:
            _w = word[0] + "".join(random.sample(word[1:-1:],
                                                 len(word) - 2)) + word[-1]
            result.append(_w)
        else:
            result.append(word)
    return " ".join(result)


string = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typoglycemia(string))
