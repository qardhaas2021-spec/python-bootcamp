# python tuples
# tuples are immutable sequences of objects
# tuples are defined using parentheses

t1 = tuple()
t2 = ()
print(type(t1), type(t2))

x = 10, 20, 30
print(type(x))
print(x[2])
print(x[-1])
print(x[0])


t1 = (20, 'abc', True)
print(t1)
print(type(t1))

students_score = 70, 60, 50, 55, 62, 58
print(students_score)
print(type(students_score))

t1 = (10)
print(type(t1))


t2 = (2, 3)
print(type(t2))

t3 = 10, 'abc', True
print(type(t3))
print(id(t3))

t5 = (1,)
print(type(t5))

l1 = list(t3)
print(l1)

