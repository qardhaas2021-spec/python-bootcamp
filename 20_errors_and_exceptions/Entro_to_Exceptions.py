# PYTHON ERRORS AND EXCEPTION HANDLING
# In python there are two types of Errors
# 1. Syntax(parsing) Errors
# 2. Exceptions(runtime errors)

# Syntax Errors are errors in the code that prevent the code from running.
# Exceptions are errors in the code that occur during runtime.

# for x in range(10)
#    print(x) # this is syntex errors becouse i skip the collon simple after the range

# d1 = {"a": 4}
# print(d1["b"]) # this is a exception error becouse there is no key b in the dictionary

for x in range(10):
    print(x)

# for x in range(1, 11):
# print(x) # this is expections or  a runtime error becouse the for indentation

for x in range(1, 11):
      print(x)

from pathlib import Path

with open("myfile.txt") as f:
    print(f.read())

# with open("myf.txt") as f:
#     print(f.read()) # this is a exception error becouse there is no file to read

# a, b = 10, 0
# print(a / b) # this is a exception error becouse i am deviding by zeroDivisionError
#  ORR
# print(a + "10") # this is type Error

a = int("10")
print(a + 10)
try:
    d1 = {"a": 4}
    print(d1["b"])
except KeyError:
    print("That key does not exist in the dictionary")


