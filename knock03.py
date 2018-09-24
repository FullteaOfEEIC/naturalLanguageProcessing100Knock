string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
string = string.replace(",", "")
string = string.replace(".", "")


result = [len(i) for i in string.split(" ")]
print(result)
