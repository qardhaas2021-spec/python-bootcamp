# THE RETURN STATEMENT


def add1(a, b):
    print(f"sum:{a + b}")


def add2(a, b):
    return a + b


add1(5, 5)
my_sum = add2(2, 2)
print(my_sum)


def add3(x, y, z):
    return x + y +z 

    
add3(4, 6, 10)
my_sum = add3(4, 6, 10)
print(my_sum)

def my_func(x):
    return  x, x**2, x**3, 

my_func(2)
print(my_func(2))
a, b, c,  = my_func(2)
print(a, b, c, )
x, *y = my_func(4)
print(x, y)


def multiply(a, b):
    return a * b


result = multiply(10, 10)
print(result)


def maxmin(a, b):
    if a < b:
        return a, b
    else:
        return b, a


small, big = maxmin(8, 3)
print(f"small: {small} \nbig: {big}")


def is_positive(number):
    if number > 0:
        return True
    else:
        return False


print(is_positive(10))
print(is_positive(-10))


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(8))
print(is_even(9))


def evearage(a, b, c):
    return (a + b + c) / 3


mean = evearage(10, 20, 30)
print(mean)


def calculate_discount(price, discount):
    return price * discount
    if price > 100:
        return price * 0.1
    else:
        return price * 0.05


discountted_price = calculate_discount(100, 0.1)
print(discountted_price)

def get_vat(price, vat):
     return (price * vat) / 100


vat = get_vat(200, 10)
print(vat)


def add(price, tax):
    return price + tax

totol = add(200, 10)
print(totol)

new_totol = add(200, 10) + add(300, 20) / 2
print(new_totol)


