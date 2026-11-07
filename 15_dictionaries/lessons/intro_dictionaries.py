# DICTIONARIES IN PYTHON

person = {'name': 'Ahmed', 'age': 28, (1, 2, 3): 100}
print(type(person))

#  create empty dectionaries

d1 = dict()
d2 = {}
print(type(d1), type(d2))

# working with dectonaries in python

person = {'name': 'Ahmed', 'age': 28, (1, 2, 3): 100}
print(len(person))

# DECTIONNRIES ARE MUTABLE DATA TYPE YOU CAN REMOVE OR ADD DATA

person['name'] = 'Ali'
print(person)

person['city'] = 'cairo'
print(person)

personal_info = {'name': 'Ahmed', 'age': 28, 'city': 'sligo'}
personal_info['satatus'] = 'single'
personal_info['job'] = 'developer'
print(personal_info)

city = personal_info['city']
print(city)

value = personal_info.get('country', 'key does not exist')
print(value)

# we can also use .pop() to remove item

name = personal_info.pop('name')
print(name, personal_info)

# ANOTHER METHID IS POPITEM() it removes and retunes the last inserted

print(personal_info.popitem())

# we can use del[] statment to remove item

del personal_info['city']
print(personal_info)

# nasted dictionries

somalia = {

    'cities': ['mugadisho', 'hargeisa', 'bosaso', 'galkacyo'],
    'info': {'population': 15_000_000, 'formar_president':
    ['hassan sheekh mahamud.', 'shekh sharid', 'mohamed siad barre', 'farmaajo']},
    'famous_artists': ['hassan aadan samatar', 'maxamed sulaiman tubeec', 'cabdi tahliil warsame'],
    'tourist_attractions': ['suurad', 'liido beach', 'jaziira beach']
}

print(somalia['cities'][0])
print(f"the former presidents of somalia {somalia['info']['formar_president'][0]}")
print(f"the famous artist in somalia is {somalia['famous_artists'][0]}")
attraction = somalia['tourist_attractions'][2]
print(f"the most visited tourist attraction in somalia is {attraction}")


usa = {
    'cities': ['new york', 'los angeles', 'chicago', 'houston'],
    'info': {
        'population': 330_000_000,
        'former_president': ['george w. bush', 'barack obama', 'donald trump']
    },
    'geography': {
        'capital': 'washington d.c',
        'largest_city': 'new york',
        'currency': 'usd'
    }
}
print(usa['cities'][1])



spain = {
    'cities': ['madrid', 'barcelona', 'valencia', 'sevilla'],
    'info': {'population': 47_000_000, 'capital': 'madrid', 'currency': 'euro'},
    'famous_places': {
        'landmarks': ['sagrada familia', 'barcelona cathedral', 'santiago de compostela'],
        'people': ['spanish', 'catalan', 'portuguese']
    }
}

print(spain['cities'][1])
print(spain['famous_places']['landmarks'][2])

product = {'id': 1234, 'name': 'iphone'}
product['seller'] = 'apple'
product['price'] = 1000
print(product)

model = {'car': 'toyota', 'model': 'camry', 'color': 'red', 'year': 2028,
         'keys': ['key 1', 'key 2', 'key 3'], 'engine': 'v8', 'owner': 'Ahmed'}
print(model['car'], model['keys'][2], model['model'], model['year'], model['owner'])
 

model = {'car': 'bmw', 'owner': 'Ahmed'}
model['color'] = 'blue'
model['year'] = 2020
model['keys'] = ['key 1', 'key 2', 'key 3']
model['engine'] = 'v6'
print(model)


student = {'name': 'Ahmed', 'grade': 'B'}
student['school'] = 'Macmuur'
student.update({'grade': 'A'})

print(student)


student = {'Name': 'Ali', 'Grade': 'B'}
student.update({'Grade': 'A', 'School_name': 'Macmuur', 'Age': 30})
print(student)


phone = {'brand': 'samsung', 'price': 800, 'color': 'black', 'discount': 50}
phone.pop('discount')
print(phone)

phone.popitem()
print(phone)



