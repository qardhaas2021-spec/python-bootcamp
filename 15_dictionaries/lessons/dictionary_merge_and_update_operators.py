# DICTIONARY MERGE(|) AND UPDATE (|=) OPERATOER

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'d': 4, 'b': 5, 'e': 6}
d3 = d1 | d2
print(d3)

d1 |= d2
print(d1)

my_shoping = {'apple': 10, 'banana': 20, 'cherry': 30}
my_fr_shoping = {'eggs': 15, 'banana': 25, 'bread': 35}
final_shoping = my_shoping | my_fr_shoping
print(final_shoping)

my_shoping |= my_fr_shoping
print(my_shoping)

