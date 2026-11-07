# SET AND DICT COMPERHENSTION
di = {'a': 1, 'b': 2, 'c': 4}
di = {k*2: v*2 for k, v in di.items()}
print(di)

# nums = [1, 2, 3, 4, 5]
# squres = {n * n for n in nums if n % 2 == 0}
# print(squres)

# nums = [2, 4, 6, 8, 10]
# squares = set()
# for n in nums:
#     squares.add(n * n)
#     print(nums)


squares = {n * n for n in [2, 4, 6, 8, 10]}
print(squares)


numes = {'ahmed', 'mohamed', 'omar', 'ali'}
names = {n.capitalize() for n in numes}
print(names)
print({n.upper() for n in numes if n.startswith('a')})

shoping = {
    'a': 1,
    'b': 2,
    'c': 3
}
shoping = {k*2: v for k, v in shoping.items()}
print(shoping)

shoping = {k.upper(): v*2 for k, v in shoping.items() if v % 3 == 0}
print(shoping)


# zip 

years = [2021, 2022, 2023, 2024, 2025]
revenue = [1000, 2000, 3000]
z = zip(years, revenue)
sales = list(z)
print(sales)

my_sales = dict(zip(years, revenue))
print(my_sales)

profit = {k: v*0.15 for k, v in my_sales.items()}
print(profit)

nums = [1, 2, 3, 4, 5]
squares = {n * n for n in [1, 2, 3, 4, 5] if n > 2}
print(squares)

prices = {'apple': 10, 'banana': 20, 'cherry': 30}
my_dict = {k: v + 5 for k, v in prices.items()}
print(my_dict)

codes = {'a': 1, 'b': 2, 'c': 3}
my_codes = {k.upper(): v for k, v in codes.items()}
print(my_codes)

students = ['Ahmed', 'Sara', 'Omar']
grades = ['A', 'B', 'c']
Z = zip(students, grades)
students_grades = dict(Z)
print(students_grades)

my_students = {k: v for k, v in students_grades.items() if v == 'A'}
print(my_students)


years = [2021, 2022, 2023, 2024]
revenue = [1000, 2000, 3000, 4000]
sales = dict(zip(years, revenue))
profit = {k: v*0.2 for k, v in sales.items() if v*0.2 > 500}
print(sales, profit)

old = {'milk': 2, 'bread': 1}
new = {'eggs': 3, 'bread': 2}
old_new = old | new
print(old_new)
my_old_new = {k: v*2 for k, v in old_new.items()}
print(my_old_new)




















