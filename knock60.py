import plyvel
import json
from tqdm import tqdm

db = plyvel.DB("./artist.ldb", create_if_missing=True)
if __name__ == "__main__":
    with open("artist.json") as fp:
        for line in tqdm(fp):
            data = json.loads(line)
            name = data["name"]
            area = data.get("area", "None")  # Noneでは動かない
            db.put(name.encode("utf-8"), area.encode("utf-8"))
