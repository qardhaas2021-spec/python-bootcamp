# lambda expressions are a way to create anonymous expression functions
# they are defined using the lambda keyword
# they are used to create small functions that are not defined in the main code


def add(a, b, c):
    result = a + b + c
    return result


result = (lambda a, b, c: a + b + c)(10, 10, 10)
print(result)


# example 2

square = lambda x: x ** 2
print(square(5))


price = [10, 20, 30]
doubled = list(map(lambda x: x * 2, price))
print(doubled)

price = [10, 20, 30]
with_tax = list(map(lambda p: p + (p * 0.05), price))
print(with_tax)

names = ['Ahmed', 'Ali', 'Omar']
uppercase = list(map(lambda name: name.upper(), names))
print(uppercase)

celsius = [0, 10, 25]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)


scores = [70, 80, 90]
bonus_scores = list(map(lambda score: score + 5, scores))
print(bonus_scores)


prices = [100, 200, 50]
sale = list(map(lambda p: p - (p * 0.10), prices))
print(sale)

words = ['python', 'sql', 'code']
lengths = list(map(lambda words: len(words), words))
print(lengths)

price = [5, 15, 25]
doubled = list(map(lambda p: p * 2, price))
print(doubled)

number = [20, 25, 30]
add_numbers = list(map(lambda n: n + 10, number))
print(add_numbers)

names = ['ahmed', 'sara', 'ali']
title = list(map(lambda name: name.title(), names))
print(title)


bill = [40, 60, 80]
tips = list(map(lambda b: b + (b * 0.15), bill))
print(tips)

kg = [1, 2.5, 0.5]
grams = list(map(lambda k: k * 1000, kg))
print(grams)

kg = [1, 2.5, 0.5]
for k in kg:
    print(k * 1000)
print('--------------------------------')

meteres = [1, 2, 3]
cm = list(map(lambda m: m * 10000, meteres))
print(cm)

meteres = [1, 2, 3]
for m in meteres:
    print(m * 10000)
print('--------------------------------')

prices = [10, 20, 30]
discounted = list(map(lambda p: p - (p * 0.20), prices))
after_discount = list(map(lambda p: p - (p * 0.10), prices))
print(after_discount)


