# CONDITIONAL STATEMENT
balance = 100
price = 50
if balance >= price:
    new_balance = balance - price
    print(
        f"you can book the flight and your new balance will be "
        f"{new_balance}."
    )
else:
    print(f"Ensufficen funds! please deposit {price - balance}")

print("Other instarctions.....")

marks = 80
fail_mark = 40
if marks >= fail_mark:
    pass_result = marks - fail_mark
    print(
        f"you have passed the exam and your new pass result will be "
        f"{pass_result}."
    )
else:
    print(
        f"you have failed the exam and your new fail result will be "
        f"{marks - fail_mark}"
    )

# print("Thank you for youe lissning system.....")

# price = 80
# quantity = 2
# discount = 10
# if quantity > 1:
#     discount_price = price * discount / 100
#     real_price = price - discount_price
#     print(f"you have a disccount of {discount_price} and you real price will be {real_price}")
# elif quantity == 1:
#     print(f"you have no discount")


# print('other instractions......')

# correct_password = 1234
# attempt = 3

# while attempt > 0:
#     password = int(input('Enter your password: '))

#     if password == correct_password:
#         print('login is successful')
#         break
#     else:
#         attempt = attempt - 1
#         print(f"you have {attempt} attempts left")

# if attempt == 0:
#     print("your account is locked please contact the bank")


# computer_password = 'Ahmed123'
# attempt = 3
# while attempt > 0:
#     password = input("Enter your password: ")
#     if password == computer_password:
#         print("loging is successful")
#         break
#     else:
#         attempt = attempt - 1
#         print(f"you have {attempt} attempt left")
#     if  attempt == 0:
#         print("Your computer is locked please contact the repair shop")

numbers = range(10, 21)
for n in numbers:
    if n % 2 == 0:
        print(n)



numbers = range(10)
for n in numbers:
    if n % 2 == 0:
        print(n)

        
# student = (input("Enter your student Subject: "))
# if student == "Math":
#     print("you are a math student")
# elif student == "Science":
#     print("you are a science student")
# else:
#     print("Your are not a student")

answer = input("Enter de you wanna continue: ")
if answer == "yes":
    print("we'll continue: ")
elif answer == "no":
    print("we'll stop: ")
else:
    print("Invalid answer")

