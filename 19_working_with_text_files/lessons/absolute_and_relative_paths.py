# ABSOLUTE AND RELATIVE PATHS
# from pathlib import Path

# # Relative path

# f = open("sittings.txt")
# contantes = f.read()
# print(contantes)
# f.close()

# f = open(Path(__file__).parent / "sittings.txt")
# contantes = f.read()
# print(contantes)
# f.close()

# from pathlib import Path
# f = open(Path(__file__).parent / "configuration.txt")
# content = f.read()
# print(content)
# f.close()

# . >= current working directory
# .. >= parent directory
# open("configuration.txt")  # relative: only works if CWD is this folder

from pathlib import Path
f = open(Path(__file__).parent / 'configuration.txt')
content = f.read()
print(content)
f.close()
