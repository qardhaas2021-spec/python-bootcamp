def greet():
    print("Hello, Ahmed")

say = greet
say()


def double(x):
    return x * 2

def apply(fn, value):
    return fn(value)

print(apply(double, 5))


def shout(word):
    return word.upper()

print(apply(shout, "ahmed"))


def to_lower(word):
    return word.lower()


print(apply(to_lower, "AHMED"))
