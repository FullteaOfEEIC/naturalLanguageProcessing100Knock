from knock20 import uk
import re

category = re.compile("\[\[Category:(.)*\]\]")

for text in uk().split("\n"):
    if category.search(text):
        print(text)
