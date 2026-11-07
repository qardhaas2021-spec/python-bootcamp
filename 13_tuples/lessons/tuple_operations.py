# TUPLE OPERATIONS
# 1. CONCATENATION USING + OPERATOR
my_tuble = ('cofee', 'tea', 'late')
my_tuble2 = my_tuble + ('water', 'juice')
print(my_tuble2)

# 2: Repetation using * operator
price = (2, 'acb', 'xyz') * 2
print(price)

print(my_tuble[0:2])
print(my_tuble[1:])
print(my_tuble[::])

dirinking = ('coffee', 'tea', 'latee')
for d in dirinking:
    print(f'we are drinking {d}')

# 3: Membership of elements uning in or in operator
print('coffee' in dirinking)
print('water' not in dirinking)

# 4: Iteration using for loop
for d in dirinking:
    print(d)
 
