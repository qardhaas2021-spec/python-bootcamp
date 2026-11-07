# FUNTION AND POSITIONAL KEY KEYWORD ARGUMENTS

def difference(a, b):
    result = a - b
    print(result)


difference(10, 5)


# paramentres & arguments

def func1(x, y, z):
    print(f"1st parametres is {x}")
    print(f"2nd parametres is {y}")
    print(f"3rd parametres is {z}")


func1(y=10, x=20, z=30)


def func2(a, b, c):
    a = a + 10
    b = b + 20
    c = c + 20
    print(a, b, c)


func2(2, 3, 4)


def func3(name, age, city):
    print(f"my name is {name}.")
    print(f"i am {age} years old.")
    print(f"i live in {city}.")


func3("ahmed", 25, "sligo")


def my_score(math, science, english):
    """This is the fiction score of the student."""
    print(f"my math score is {math}.")
    print(f"my science score is {science}.")
    print(f"my english score is {english}.")


print(my_score.__doc__)
my_score(97, 88, 92)


# Real math: mean, median, mode from a LIST of scores
import statistics


def calculate_average(scores):
    """Calculate mean, median, and mode from student scores.

    Args:
        scores: A list of numbers, e.g. [90, 88, 92, 88, 95]

    Returns:
        None (prints the results)
    """
    mean = statistics.mean(scores)      # average
    median = statistics.median(scores)  # middle value
    mode = statistics.mode(scores)      # most common value

    print(f"scores: {scores}")
    print(f"mean (average): {mean}")
    print(f"median (middle): {median}")
    print(f"mode (most common): {mode}")


calculate_average([90, 88, 92, 88, 95])
