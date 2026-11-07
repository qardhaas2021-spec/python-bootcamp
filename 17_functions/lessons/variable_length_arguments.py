# variable length arguments


def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


result = add(1, 2, 3, 4, 5)
print(result)


def show(*numbers):
    return sum(numbers)

    print(numbers)


result = show(10, 20, 30)
print(result)

t1 = show(100, 100)
print(t1)


def show2(a, b , c):
    return a + b + c

result = show2(5, 5, 5)
print(result)

def show_pack(*numbers):
    print(numbers)
    print(type(numbers))


show_pack(1, 2, 3)
show_pack(10, 20)

def show_bag(*items):
    print("In your bag")
    print(items)


show_bag("apple", "banana", "cherry")
show_bag("phone", "charger")


def total_bill(*prices):
    return sum(prices)


print(total_bill(2.50, 1.20, 3.00))
print(total_bill(10, 15, 8, 4))


def invite_guest(*names):
    print("Guests Invited:")
    for name in names:
   
     print("-", name)
    
invite_guest("Ahmed", "mahad", "Amiin")






  

