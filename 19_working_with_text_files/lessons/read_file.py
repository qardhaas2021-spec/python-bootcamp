# Oening and reading files

from pathlib import Path

f = open(Path(__file__).parent / "configuration.txt", "rt")
content = f.read()
print(content)
print(f.closed)
f.close()
print(f.closed)

f = open("configuration.txt", "rt")
content = f.read()
print(content)

folder = Path(__file__).parent

f1 = open(folder / "sitting.txt")
print(f1.read())

f2 = open(folder / "sittings.txt")
print(f2.read())

from pathlib import Path
f1 = open(folder / "sitting.txt")
print(f1.read())

f2 = open(folder / "sitting.txt")
print(f2.read())
