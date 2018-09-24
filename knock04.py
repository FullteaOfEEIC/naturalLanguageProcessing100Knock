string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

separated = string.split(" ")
result = {}

for i, word in enumerate(separated):
    if i + 1 in (1, 5, 6, 7, 8, 9, 15, 16, 19):
        result[word[0]] = i + 1
    else:
        result[word[0:2:]] = i + 1

print(result)
