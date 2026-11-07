# PYTHON LISTS

l1 = [1, 28.5, 'python', 'true', ['abc', 'ahmed'], (10, 30, 20)]
print(len(l1))

l2 = []  # empty list
l3 = list()  # empty list
print(l1[0])

x = l1[-1]
print(x)

l4 = l1[4]
print(l4)
print(id(l4))
l4[0] = 'x'
l4.append(100)
print(l4)
print(id(l4))

l1 = ['python', [1, 2], 'javal', 30,[2,3]]
print(l1[0][-1])

