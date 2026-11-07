import sys
import os
from datetime import datetime
import math
import random
import json


print(sys.version)
print(sys.platform)
print(sys.path)

if sys.platform == "darwin":
    print("you are using macOS")
elif sys.platform == "win32":
    print("you are using windows")

print(os.getcwd())
print(os.listdir())
print(len(os.listdir(".")))


from datetime import datetime
now = datetime.now()
print(now)
print(now.strftime("%H:%m"))
if now.hour < 12:
    print("Good morning")
else:
    print("Good afternoon")

number = 81
print(math.sqrt(number))
if number % 2 == 0:
    print("Even")
else:
    print("Odd") 

students = ["Ahmed", "Sara", "Tom"]
print(random.choice(students))

user = {"name": "Ahmed", "age": 30}
with open("user.json", "w") as f:
    json.dump(user, f)
with open("user.json") as f:
    data = json.load(f)

print(data["name"])


orders = [
    {"items": ["apple", "banana", "cherry"], "total": 100},
    {"items": ["milk", "bread", "eggs"], "total": 50},
    {"items": ["coca", "pepsi", "sprite"], "total": 20},

]

today = datetime.now().today()
sales = orders[0]["total"] + orders[1]["total"] + orders[2]["total"]

print(f"Date: {today}")
print(f"Number of orders: {len(orders)}")
print(f"Total sales: {sales}")

with open("orders.json", "w") as f:
    json.dump(orders, f, indent=2)


orders = [
    {"items": ["keyboard", "mouse"], "total": 45, "due": "2026-09-10"},
    {"items": ["A4 paper", "pens"], "total": 12, "due": "2026-09-20"},
    {"items": ["cleaning sprey"], "total": 8, "due": "2026-09-14"}

]

sales = orders[0]["total"] + orders[1]["total"] + orders[2]["total"]
today = datetime.now().date()
for order in orders:
    due_date = datetime.strptime(order["due"], "%Y-%m-%d").date()
    if due_date < today:
        status = "late"
    else:
        status = "on time"
    print(f"{order['items']} due {order['due']} {status}")