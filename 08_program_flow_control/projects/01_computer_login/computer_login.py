# Computer Login — Flow Control Mini Project
# Uses: while loop, if/else, break, attempt counter

computer_password = "Ahmed123"
attempt = 3

while attempt > 0:
    password = input("Enter your password: ")

    if password == computer_password:
        print("Login is successful")
        break
    else:
        attempt = attempt - 1
        print(f"You have {attempt} attempt(s) left")

    if attempt == 0:
        print("Your computer is locked. Please contact the repair shop.")
