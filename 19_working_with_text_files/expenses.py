# # EXPENSES APP - practice read + write + total
# from pathlib import Path
# from datetime import date

# expenses_file = Path(__file__).parent / "expenses.txt"

# # 1) Ask for item and price (number only, example: 4)
# # item = input("What did you buy? ")
# # price = float(input("How much did it cost? (number only) "))

# # 2) Save (append) the expense with today's date
# with open(expenses_file, "a") as f:
#     f.write(f"{date.today()}: {item} - {price}\n")

# print("Saved!\n")

# # 3) Read all expenses and calculate total
# total = 0.0

# print("--- My Expenses ---")
# with open(expenses_file) as f:
#     for line in f:
#         line = line.strip()
#         if not line:
#             continue
#         print(line)
#         # Try to read the number after " - "
#         try:
#             amount = float(line.split(" - ")[-1])
#             total += amount
#         except ValueError:
#             # Skip old lines that are not a clean number
#             pass

# print(f"\nTotal expenses: {total}")


expenses = {"rent": 550, "food": 300, "transportation": 100, "phone": 20,
            "fun": 100}

income = 2700

total = sum(expenses.values())
saved = income - total


print(f"Total spent: €{total}")
print(f"Saved: €{saved} ({saved / income:.0%} of income)")