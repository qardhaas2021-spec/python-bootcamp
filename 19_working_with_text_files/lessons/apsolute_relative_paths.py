# ABSOLUTE AND RELATIVE PATHS

from pathlib import Path

f = open("19_working_with_text_files/lessons/sitting.txt")  # Relative path
content = f.read()
print(content)


f = open(
    "/Users/mijnmacbook1/Documents/Python Learning/python_bootcamp/"
    "19_working_with_text_files/lessons/sitting.txt"
)  # Absolute path
content = f.read()
print(content)
f.close()

folder = Path(__file__).parent
file = open(folder / "sitting.txt")
content = file.read()
print(content)
