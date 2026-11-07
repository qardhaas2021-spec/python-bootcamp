import csv

item = input("Enter the item: ")
price = input("Enter the price: ")

if not price.isdigit():
    print("Price must be a number")
else:
    with open("expenses.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([item, price])
    print("Saved!")

total = 0
most_expensive = 0
most_item = ""

with open("expenses.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    print("\nyour expenses:")
    for row in reader:
        print(f"{row[0]}: {row[1]}")
        total += int(row[1])
        price = int(row[1])
        if price > most_expensive:
            most_expensive = price
            most_item = row[0]
        

print(f"total: {total}")
print(f"Most expensive: {most_item}, {most_expensive}")
