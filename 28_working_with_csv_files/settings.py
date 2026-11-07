import json

with open("settings.json", "rt") as f:
    obj = json.load(f)

print(f"Welcome back {obj["Name"]}, you are on level {obj["Level"]}")

    