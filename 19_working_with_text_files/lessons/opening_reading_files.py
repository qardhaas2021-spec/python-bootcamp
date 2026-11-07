# there are two types of file
# 1. text file
# 2. binary file

f = open("working_with_text_files.py", "rt")
content = f.read()
print(content)
print(f.closed)
f.close()
print(f.closed)






