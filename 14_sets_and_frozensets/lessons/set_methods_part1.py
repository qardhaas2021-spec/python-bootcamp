#  SET METHODS
#  1. set.add()

s1 = {1, 2, 3, }
s1.add('a')
s1.add(2.5)
print(s1)


# 2. SET.REMOVE(ITEM)

s1.remove('a')
print(s1)
s1.remove(2.5)
print(s1)

# 3. set.discard()
s1.discard(2)
print(s1)


# 4.set.pop()
s2 = {1, 2, 'abc', 2.5, 'x', 2}
x = s2.pop()
print(x)
print(s2)


order = ['pizza', 'burger', 'pasta', 'salad', 'sushi']
next_order = order.pop(0)
print(f'now preparing {next_order}')
print(f'still waiting for {order}')
l1 = order.pop(2)
print(f'{l1} is ready')
print(f'{order} is still waiting queue')


l1 = set('abc')
l2 = l1
l1.add('d')
print(l1)

# 5. set.clear()

l2.clear()
print(l2, l1)

# 6. set.copy()
l3 = l1.copy()
l3.add('e')
print(l3, l1)


# 7. set.update()

x1 = {1, 2, 3}
x1.update([4, 5, 6])
print(x1)

# 8. set.union()
a = {1, 2, 3}
b = {4, 5, 6}
print(a.union(b))

s1 = set('helloooo')
print(len(s1))


