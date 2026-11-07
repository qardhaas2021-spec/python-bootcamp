import sys

stock = {
    "keyboard": 12,
    "mouse": 40,
    "paper": 3,
}

if len(sys.argv) < 2:
    print("Usage: python stock.py keyboard")
else:
    item = sys.argv[1]
    if item in stock:
        print(f"{item}: {stock[item]} in warehouse")
    else:
        print(f"{item}: not in warehouse")
