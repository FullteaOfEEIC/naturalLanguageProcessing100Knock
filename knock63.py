import plyvel
import json
from tqdm import tqdm
import sys

db = plyvel.DB("./knock63.ldb", create_if_missing=True)

if __name__ == "__main__":
    with open("artist.json") as fp:
    for line in tqdm(fp):

            data = json.loads(line)
            name = data["name"]
            tags = data.get("tags", [])
            db.put(name.encode("utf-8"), json.dumps(tags).encode("utf-8"))

    if len(sys.argv)>1:
        artist=" ".join(sys.argv[1::])
        print(json.loads(db.get(artist.encode("utf-8")).decode()))
