from knock20 import uk
import re

category = re.compile("\[\[Category:((.)*)\]\]")

for text in uk().split("\n"):
    m = category.search(text)
    if m:
        print(m.group(1))
