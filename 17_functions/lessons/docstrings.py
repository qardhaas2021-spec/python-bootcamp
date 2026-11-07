# docstring is a string that is used to describe the function

def say_hello(name):
    """this function says hello to you!
    
    this is multiline doc string.
    
    it can be used to describe the function and its parameters and return value.
    """
    print(f"hello {name}!")


say_hello("Ahmed")
print(say_hello.__doc__)


def calculate_area(width, height):
    """Calculate the area of a rectangle.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.
   

    Returns:
        The area (width * height).
    """
    print(f"the area of the rectangle is {width * height}")
    return width * height


print(calculate_area(5, 10))


def calculate_price(price, text):
    """calculate the price of a product with tax."""
    price = 100
    """calculate the price of a product with tax."""
    text = '10%'
    final_price = price + (price * text)
    return final_price


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


print(add(10, 10))
print(add(3, 7))
print(add.__doc__)


def my_name(name):
    """Return given name."""
    return name


print(my_name('Ahmed'))


def greet(name):
    """Print a greeting to the given name."""
    print(f"hello {name}")


greet('Ahmed')


def is_even(number):
    """Check if the given number is even or odd."""
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(10))
print(is_even(11))
print(is_even.__doc__)


def calculate_discount(price, discount_percentage):
    """Calculate the final price after a discount.

    Args:
        price: The original price.
        discount_percentage: The discount percentage (e.g. 10 for 10%).

    Returns:
        The final price after discount.

    Example:
        calculate_discount(100, 10) -> 90
    """
    return price - (price * discount_percentage / 100)

print(calculate_discount.__doc__)
print(calculate_discount(100, 10))
