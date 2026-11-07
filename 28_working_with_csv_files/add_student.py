import json

with open("student.json", "r") as file:
    data = json.load(file)
name = input("Enter the name: ")
age = int(input("Enter the age: "))
data.append({"Name": name, "Age": age})

with open("student.json", "w") as file:
    json.dump(data, file, indent=2)
    print("Student added successfully")
