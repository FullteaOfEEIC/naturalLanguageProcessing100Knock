from knock60 import db
import sys

if len(sys.argv)==1:
    print("please specify artist")
    sys.exit()

artist = " ".join(sys.argv[1::])
print(db.get(artist.encode("utf-8")).decode())
