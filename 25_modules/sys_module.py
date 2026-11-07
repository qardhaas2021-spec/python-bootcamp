# import sys

# print(sys.version)
# help("modules")

# print(sys.path)
# print(f"current python version: {sys.version}")

# ADVANCED IMPORT TECHNIQUES

# import random

# for i in range(4):
#     print(random.randint(1, 100))

# print(random.choice(["apple", "banana", "orange"]))

# from random import randint, choice
# print(randint(1, 100))
# print(choice(["apple", "banana", "orange"]))

import random as rnd
import math as m
import datetime as dt

print(rnd.randint(1, 100))
print(rnd.choice(["apple", "banana", "orange"]))
print(m.sqrt(16))

print(m.acos(0.5))
print(dt.datetime.now())


def greet(name):
    return f"Hello, {name}1"


def add(a, b):
    return a + b



