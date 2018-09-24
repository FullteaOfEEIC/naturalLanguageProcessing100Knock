from knock05 import n_gram

paradise = "paraparaparadise"
paragraph = "paragraph"

X = set()
Y = set()
for i in n_gram(paradise, 2):
    X.add(i)
for i in n_gram(paragraph, 2):
    Y.add(i)

print("X+Y={}".format(X | Y))
print("X&Y={}".format(X & Y))
print("X-Y={}".format(X - Y))

print("'se' is in X:{}".format("se" in X))
print("'se' is in Y:{}".format("se" in Y))
