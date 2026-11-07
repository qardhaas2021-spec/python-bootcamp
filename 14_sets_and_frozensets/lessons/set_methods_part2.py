set1 = {1, 3, 5,}
set2 = {5, 7, 9}

#  set.intersection()
set3 = set1.intersection(set2)
print(set3)

#  other methos use &

set3 = set1 & set2
print(set3)


# 2. set.deffrence()
set4 = set1.difference(set2)
print(f'{set4} is the diffrence of set1 and set2')

# use - operator
set4 = set1 - set2
print(set4)

# set4 = set1.difference([1,2, 3, 4, 5])
# set4 = set1 - [1, 2, 3, 4, 5] ERROR

# 3. SET.SYMETRIC_DEFFRENCE()

s5 = set1.symmetric_difference(set2)
print(s5)


# use ^ operator

s5 = set1 ^ set2
print(s5)

# set.union()

s6 = set1.union(set2)
print(s6)

# use vertical bar | operator

s6 = set1 | set2
print(s6)


# 5. set.disjoint
x = {1, 2, 3, 5}
y = {4, 5, 7, 8}
print(x.isdisjoint(y))

