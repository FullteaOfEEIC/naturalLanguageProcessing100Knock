from knock28 import template28
import requests
import json

fileName = template28()["国旗画像"]
endpoint = "https://en.wikipedia.org/w/api.php"
params = {"action": "query", "prop": "imageinfo", "iiprop": "url",
          "format": "json", "titles": "File:{}".format(fileName)}
result = requests.get(endpoint, params=params)
print(json.loads(result.text)["query"]["pages"]
      ["23473560"]["imageinfo"][0]["url"])
