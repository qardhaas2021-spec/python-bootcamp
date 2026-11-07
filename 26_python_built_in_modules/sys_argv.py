# import sys

# print("all", sys.argv)
# print("Script:, sys.argv[0]")

# if len(sys.argv) > 1:
#     name = sys.argv[1]
#     print(f"Hello, {name}!")
# else:
#     print("Usage: python3 hello.py Ahmed")

import sys
print(f"Arguments: {len(sys.argv)}")
print(f"This is name of script: {sys.argv[0]}")
print(f"The script arguments are: {sys.argv}")
print(f"The script arguments are: {sys.argv[1:]}")

if len(sys.argv) >= 2:
    for item in sys.argv[1:]:
        with open(item, "r") as f:
            print(f.read())
else:
    print("wrong number of arguments")