def cipher(text):
    result = ""
    for t in text:
        if ord(t) - ord("a") >= 0 and ord(t) - ord("a") < 26:
            result += chr(219 - ord(t))
        else:
            result += t
    return result


print(cipher(cipher("this is a pen")))
