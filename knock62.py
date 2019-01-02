from knock60 import db

count = 0
for key, value in db:
    if value == "Japan".encode("utf-8"):
        count += 1

print(count)
