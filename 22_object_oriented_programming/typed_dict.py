# typedDict

from sys import version
from typing import TypedDict


class User(TypedDict):
    name: str
    age: int        # this is class attributes
    height: float


user: User = {
    "name": "Ahmed",
    "age": 20,
    "height": 1.75
}
print(user["name"])
user["height"] = 1.80
print(user["height"])

def get_user(user: User) -> None:
    print(f'user: {user["name"]}')
    print(f'age: {user["age"]}')
    print(f'height: {user["height"]}')


get_user({"name": "Ali", "age": 20, "height": 1.65})
print(get_user)


class car(TypedDict):
    brand: str
    model: str
    year: int
    price: float
    color: str

s1: car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020,
    "price": 10000,
    "color": "Red"
    }
print(s1["brand"])
print(s1["model"])
print(s1["year"])
print(s1["price"])
print(s1["color"])


def get_car(car: car) -> None:
    print(f'brand: {car["brand"]}')
    print(f'model: {car["model"]}')
    print(f'year: {car["year"]}')
    print(f'price: {car["price"]}')
    print(f'color: {car["color"]}')


get_car({"brand": "bmw", "model": "x5", "year": 2020, "price": 280000, "color": "Balck"})
print(get_car)

class Book(TypedDict):
    title: str
    author: str
    year: int
    price: float
    version: str
    publisher: str


book1: Book = {
    "title": "Ottomic Happit",
    "author": "Ahmed",
    "year": 2020,
    "price": 18.50,
    "version": "1.0",
    "publisher": "Mohammed"
   }
print(f"title:{book1['title']}")
print(f"author:{book1['author']}")
print(f"year:{book1['year']}")
print(f"price:{book1['price']}")
print(f"version:{book1['version']}")
print(f"publisher:{book1['publisher']}")

def show_book(book: Book) -> None:
    print(f"title:{book['title']}")
    print(f"author:{book['author']}")
    print(f"year:{book['year']}")
    print(f"price:{book['price']}")
    print(f"version:{book['version']}")
    print(f"publisher:{book['publisher']}")


show_book({"title": "python programming", "author": "Mohammed", "year": 2020, "price": 18.50,
"version": 1.0, "publisher": "Ahmed"})
print(dict(book1))

book1["title"] = "rich dad poor dad"
book1["price"] = 20.50
book1["year"] = 2021
print(f"title:{book1['title']}")
print(f"price:{book1['price']}")
print(f"year:{book1['year']}")

# nasted dict

class Adress(TypedDict):
    street: str
    city: str
    zip: int


class UserWithAddress(TypedDict):
    name: str
    email: str
    adress: Adress


my_user: UserWithAddress = {
    "name": "Ahmed",
    "email": "qardhaas2021@gmail.com",
    "adress": {
        "street": "123 main st",
        "city": "sligo",
        "zip": 3535
    }
}
print(f"name:{my_user['name']}")
print(f"email:{my_user['email']}")
print(f"street:{my_user['adress']['street']}")
print(f"city:{my_user['adress']['city']}")

total_ipv6 = 2 ** 128
no_of_bits = len(str(total_ipv6))
print(f"total ipv6 addresses: {total_ipv6}")
print(f"Number of bits: {no_of_bits}")











