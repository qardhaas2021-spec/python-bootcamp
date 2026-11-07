# For loops are used to iterate over a sequence of items
# A sequence can be a list, a tuple, a dictionary, a set, or a string

# for letter in "python":  # this is a string
#     print(letter)

# for number in [1, 2, 3, 4]:  # this is a list
#     print(number)

# for number in (10, 20, 30, 40):  # this is a tuple
#     print(number * 2)

# for item in {1, "abc", 2}: # this is a set   
#     print(item)
    

    
# my_str = input("Enter something: ")
# vowels = "aeiou"
# for item in my_str:
#     if item in vowels:
#         print(item)

shoping_list = ["milk", "bread", "eggs", "rice"]
for item in shoping_list:
    print("Buy", item)

class_attendance = ["Ahmed", "Sara", "Ali", "Hassan"]
for student in class_attendance:
    print("present:", student)

price = [10, 25, 7, 40]
for item in price:
    print("$", item)

price = [12, 8, 15, 20]
total = 0
for item in price:
    total = total + item
print(total)

scores = [45, 80, 30, 95, 60]
for score in scores:
    if score >= 50:
        print("Pass")
    else:
        print("Fail")
        

numbers = range(1, 21)
for i in numbers:
    if i % 2 == 0:
        print(i, "is even")


names = ["Ali", "Fatima", "Omar"]
for name in names:
    print(name, len(name))


sentence = "I love Learning Python"
for char in sentence:
    print(char, len("I love Learning Python"))
     
multiplication_taple = (7, 8, 9, 10)
for number in multiplication_taple:
    print(number, "x", 10, "=", number * 10)

    

