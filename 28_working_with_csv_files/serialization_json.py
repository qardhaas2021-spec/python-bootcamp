import json
# json.dump saves your data to the file(this is called serialize)
# json.load reads the data back from the file (this is called deserialize)

friends = {
    "Ahmed": [28, "London", "0851909583"],
    "Maria": [27, "Paris", "0669883399"],
    "Waliid": [22, "dublin", "0831234567"]
}


with open("friends.json", "w") as f:
    json.dump(friends, f, indent=4)

json_string = json.dumps(friends, indent=4)
print(json_string)
