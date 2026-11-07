# TUPLE METHODS
# 1: tuple.index()

t1 = (1, 2, 3, 4, 5, 6, 7, 8)
x = t1.index(2)
print(f'the index of 2 is a position {x}')
y = t1.index(4)
print(y)


z = 'x'
if z in t1:
    index = t1.index(z)
    print(f'the index of {z} is in position {index}')
else:
    print(f'{z} is not in the tuple')

x = 4
if x in t1:
    index = t1.index(x)
    print(f'the index of {x} is in position {index}')

# 2: index.(count)
t2 = (1, 2, 3, 3, 3, 5, 4)
n = t2.count(3)
print(n)
print(100 in t2)

# len(), max(), min(), sum(), sorted() can be used in the tule
print(len(t2))
print(sum(t2))
print(max(t2))
print(min(t2))
print(sorted(t2))


# ═══════════════════════════════════════════════
#              TUPLE CHALLENGES
# ═══════════════════════════════════════════════

# Challenge 1 ─────────────────────────────────
# You have this tuple of temperatures:
# temps = (32, 18, 25, 40, 15, 28, 36, 22)
# Find: the highest, lowest, average temperature
# YOUR CODE HERE:

temps = (32, 18, 25, 40, 15, 28, 36, 22)
print(max(temps))
print(min(temps))
print(sum(temps) / len(temps))

temperature = [(c * 9/5 + 32) + 32 for c in temps]
print(temperature)


# Challenge 2 ─────────────────────────────────
# You have this tuple of student names:
# students = ("Ali", "Sara", "Ahmed", "Sara", "Khalid", "Ali", "Sara")
# Find: how many times "Sara" appears
# Find: the position of "Ahmed"
# YOUR CODE HERE:

students = ('Ali', 'Sara', 'Ahmed', 'Sara', 'Khalid', 'Ali', 'Sara')
print(students.count('Sara'))
print(students.index('Ahmed'))



# Challenge 3 ─────────────────────────────────
# You have this tuple of scores:
# scores = (45, 78, 90, 34, 67, 88, 55, 72)
# Create a LIST of only the scores above 60
# (hint: you need a list comprehension)
# YOUR CODE HERE:
scores = (45, 78, 90, 34, 67, 88, 55, 72)
s1 = [score for score in scores if score > 60]
print(s1)



# Challenge 4 ─────────────────────────────────
# You have this tuple:
# person = ("Ahmed", "Somalia", 1998, "Python")
# Unpack it into 4 separate variables and print each one
# YOUR CODE HERE:

person = ('Ahmed', 'Somalia', 1998, 'python')
name, country, year, language = person
print(
    f'My name is {name}, I am from {country}, '
    f'I was born in {year}, and I am learning {language}'
)




# Challenge 5 ─────────────────────────────────
# You have this tuple of prices:
# prices = (120, 45, 200, 30, 89, 150)
# Sort it from most expensive to cheapest
# Find how many prices are above 100
# YOUR CODE HERE:

prices = (120, 45, 200, 30, 89, 150)
sorted_prices = sorted(prices, reverse=True)
print(sorted_prices)
print(len([price for price in prices if price > 100]))


prices = (300, 250, 40, 20, 75, 28)
sorted_prices = sorted(prices, reverse=True)
print(sorted_prices)
print(len([price for price in prices if price > 100]))

