from knock20 import uk
import re

url = re.compile("https?://[!#$&'()*+,/:;=?%@[\]0-9a-zA-Z-._~]*")

for text in uk().split("\n"):
    m = url.findall(text)
    for u in m:
        print(u)
