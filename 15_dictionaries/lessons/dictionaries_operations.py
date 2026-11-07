cofee_shop = {
    'name': 'insomania',
    'address': '123 main st',
    'location': 'sligo',
    'hours': '9am - 5pm',
    'coffe_types': ['espresso', 'latte', 'cappuccino']
}
print(f"name: {cofee_shop['name']}\n"
      f"address: {cofee_shop['address']}\n"
      f"location: {cofee_shop['location']}\n"
      f"hours: {cofee_shop['hours']}\n"
      f"coffe types: {cofee_shop['coffe_types']}")

person = {
    'name': 'Ahmed',
    'age': 20,
    'city': 'sligo',
    'email': 'qardhaaas2021@gmail.com',
    'is_student': True
}
print(f"name: {person['name']}\n"
      f"age: {person['age']}\n"
      f"city: {person['city']}\n"
      f"email: {person['email']}\n"
      f"is_student: {person['is_student']}\n")


person = {'name': 'ahmed', 'age': 28, 'location': 'sligo'}

friend = person
person['name'] = 'ali'
print(friend)

# 1. copy() mesthod

neighbor = person.copy()
person['location'] = 'dublin'
print(neighbor, person)

# 2 .update method

countries = {'usa': 'united states of america', 'uk': 'united kingdon', 'in': 'irland'}
countries.update({'dn': 'denmark', 'fr': 'france'})
print(countries)

# 3 clear method
countries.clear()
print(countries)

#  there are three method keys, values and item that deal with keys and values of dictionaries

# 1 dict.keys()

person = {'name': 'ahmed', 'age': 28, 'location': 'sligo'}
k = person.keys()
print(k, type(k))

my_key = list(k)
print(my_key)

# 2 dict.values()
v = person.values()
print(v, type(v))
my_values = list(v)
print(my_values)

# 3 dict.item()
i = person.items()
print(i, type(i))
my_items = list(i)
print(my_items)

# 4: using in operator

'name' in person
print('name' in person)

print(10 in person.keys())

print('ahmed' in person.values())

print(('age', 29) in person.items())


print(('age', 28) in person.items())


s1 = {10: 'y', 20: 'b', 30: 'c'}
d1 = s1.values()
s1[10] = 'x'
print(d1)

t1 = {10: 'a', 20: 'b'}
t2 = {20: 'c', 40: 'd'}
x1 = t1.keys()
x2 = t2.keys()
print(x1, x2)

print(x1 & x2)
print(x1 | x2)
print(x1 ^ x2)

for k in s1:
    print(f"key is {k}")


score = {90: 'a', 75: 'b', 65: 'c', 50: 'd', 40: 'f'}
for s in score:
    print(f"score is {s}")
    
for s in score.keys():
    print(s)
for v in score.values():
    print(f"the value is {v}")
s1 = list(score.items())
print(s1)

for s in score:
    if s >= 90:
        print(f"score is {s} and grade is A")
    elif s >= 75:
        print(f"score is {s} and grade is B")
    elif s >= 65:
        print(f"score is {s} and grade is C")
    elif s >= 50:
        print(f"score is {s} and grade is D")
    else:
        print(f"score is {s} and grade is F")
 


