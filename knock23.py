from knock20 import uk
import re

section = re.compile("(==+)((.)*?)==+")

for text in uk().split("\n"):
    m = section.search(text)
    if m:
        print(m.group(2), len(m.group(1)) - 1)
