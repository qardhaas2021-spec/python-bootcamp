def greet(name):
    return f"Hello, {name}"


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


age = 20
name = "Ahmed"
if age >= 10:
    name = "Ahmed"

if __name__ == "__main__":
    print("Testing my_tools...")
    print(add(5, 3))
    print(greet("Test"))


def calculate_discount(price, quantity):
    if quantity >= 10:
        return price * quantity


def apply_discount(price, quantity, discount_percentage=10):
    subtotal = price * quantity
    discount = subtotal * (discount_percentage / 100)
    return subtotal - discount
    

def make_pizza():
    return "Pizza is ready"


if __name__ == "__main__":
    print("Testing my_tools alone")
    print(make_pizza())