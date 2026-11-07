# LISTS CANCATENATION
l1 = [1, 2, 3]
print(l1, id(l1))

l1 = l1 + [4, 5]
print(l1, id(l1))

l1 += [4, 5]
print(l1, id(l1))

l1.extend([4, 5])
print(l1, id(l1))

# there are two method that add to the end of the lists
# append . extand
l1.append(['a', 'b'])
print(l1)
l1.extend(['d', 'f'])
print(l1)
l1.append(20)
l1.extend([20])
print(l1)

# REPATITION

l2 = (['abc'])
l3 = l2 * 3
print(l3)

print('#' *10 + ' pythonslicing ' + '#' * 10)

numbers = [1, 2, 3, 4, 5]
nums = numbers[1:4]
print(f'nums:{nums}')
print(f'numbers:{numbers}')

print(numbers[:3]) # start is default zero
print(numbers[2:]) # stop is defualt the end of the list
print(numbers[1:5:3]) # step is 3
print(numbers[::2]) # step is 2
 