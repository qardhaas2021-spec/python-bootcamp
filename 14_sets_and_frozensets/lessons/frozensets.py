# PYTHON FROZENSETS
fs1 = frozenset({1, 2, 3, 'abc'})
print(fs1, type(fs1))

s1 = "python!!"
fs2 = frozenset(s1)
print(fs2)

f1 = frozenset({1, 2, 4, 5, 6,})
f2 = frozenset({2, 3, 1, 7})
f3 = f1.intersection(f2)
print(f3)

f4 = f1 | f2
print(f4)

s1 = frozenset({1, 2, 3, 4})
s2 = s1.difference(f2)
print(s2, type(s2))
print(f2, type(f2))

