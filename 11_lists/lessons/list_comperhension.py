clicks = [10, 5, 15, 20]
doubled_list = list()
for c in clicks:
    doubled_list.append(c*2)
print(doubled_list)


student_score = [70, 60, 55, 64, 83, 22]
passed_student = [s for s in student_score if s >= 60]
print(passed_student)


prodect = ['apple', 'banana', 'orange', 'orange']
cleaned_prodect = [p for p in prodect if prodect.count(p) == 1]
print(cleaned_prodect)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [n for row in matrix for n in row]
print(flattened_matrix)


ages = [22, 34, 25, 11, 15, 33, 65]
print(sum(age for age in ages if age > 20))
print([age for age in ages if age >= 20])


list = ['cofee', 'tea', 'latte', 'coffee', 'tea',
        'latte', 'coffee', 'tea', 'latte']
price = [(item, 3.5) for item in list]
print(price)


scores = [70, 60, 50, 55, 62, 58, 75, 85]
passed_doubled = [s * 2 for s in scores if s >= 50]
print(passed_doubled)


my_friends = ['ahmed jamac ', 'ahmed maxamed', 'nasrudiin halane']
s1 = [item.capitalize() for item in my_friends]
print(s1)

reversed_name = [item[::-1] for item in my_friends]
print(reversed_name)

math = [8, 18, 24, 16, 21, 25, 64]
devisible_by_eight = [m for m in math if m % 8 == 0]
print(devisible_by_eight)

math_str = [str(m) for m in math]
print(math_str)
print('-'.join(math_str))
print([item[::-1] for item in math_str])

password = [str(p) for p in range(10)]
print(''.join(password))

friends = [f.lower() for f in ['AhMed', 'MohamEd', 'Ali', 'OsmaN']]
neighbors = [n.lower() for n in ['Osman', 'Ahmed', 'Farah']]
friends_neighbors = [n for n in friends if n in neighbors]
print(friends_neighbors)

text = 'my name is ahmed and i am a student'
words = text.split()
print(words)
print([word.upper() for word in words])

# ─── Example 1: Online Store ───────────────────────────────
products = [
    {"name": "Shoes",   "price": 120, "in_stock": True},
    {"name": "Hat",     "price": 35,  "in_stock": False},
    {"name": "Jacket",  "price": 200, "in_stock": True},
    {"name": "Bag",     "price": 80,  "in_stock": True},
]
discounted = [
    p["name"] + " → $" + str(p["price"] * 0.9)
    for p in products
    if p["in_stock"]
]
print(discounted)

# ─── Example 2: School Results ─────────────────────────────
students = [
    {"name": "Ali",    "score": 45},
    {"name": "Sara",   "score": 78},
    {"name": "Khalid", "score": 90},
    {"name": "Mona",   "score": 38},
    {"name": "Omar",   "score": 65},
]
passed = [
    s["name"] + " passed with " + str(s["score"])
    for s in students
    if s["score"] >= 50
]
print(passed)

# ─── Example 3: Phone Book Cleaner ─────────────────────────
contacts = [
    {"name": "  Ahmed ",  "phone": "050 111 2222"},
    {"name": "Sara  ",    "phone": "055 333 4444"},
    {"name": "  Khalid",  "phone": "058 555 6666"},
]
cleaned_contacts = [
    {"name": c["name"].strip(), "phone": c["phone"].replace(" ", "")}
    for c in contacts
]
print(cleaned_contacts)

# ─── Your Level: Lists + List Comprehension ────────────────

countries = ["Somalia", "USA", "Brazil", "China", "UAE", "Canada"]
long_names = [c for c in countries if len(c) > 5]
short_names = [c for c in countries if len(c) <= 5]
upper_names = [c.upper() for c in countries]
print(long_names)
print(short_names)
print(upper_names)

countries = ['ethopia', 'egypt', 'Kenya', 'tanzania',
             'united states', 'united kingdom']
long_countries = [c for c in countries if len(c) > 5]
short_countries = [c for c in countries if len(c) <= 5]
upper_countreis = [c.upper() for c in countries]
print(long_countries, short_countries, upper_countreis)

age = [22, 34, 25, 11, 15, 33, 65]
adult_age = [a for a in age if a >= 18]
print(adult_age)


names = ['dan', 'mario', 'andu']
length = [len(n) for n in names if 'a' in n]
print(length)


l1 = [c.lower().upper() for c in 'abc']
print(l1)


l2 = [c.upper().lower() for c in 'hello']
print(l2)