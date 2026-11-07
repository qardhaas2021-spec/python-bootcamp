import json


items = ["nike shoes", "apple watch", "macbook pro", "iphone 15"]

with open("shopping.json", "w") as f:
    json.dump(items,  f, indent=2)

with open("shopping.json", "rt") as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)