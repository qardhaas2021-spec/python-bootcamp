# PROJECT: File Processing - read device list

with open("devices.txt") as f:
    content = f.read().splitlines()
    print(content)

devices = []
for line in content[1:]:
    devices.append(line.split(":"))
print(devices)

for device in devices:
    print("printing device: ", device[1])


for device in devices:
    print("printing device: ", device[2])
