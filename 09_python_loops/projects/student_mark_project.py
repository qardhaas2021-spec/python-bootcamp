# Student result system

name = input("Enter your name: ")

mark1 = int(input("Enter your subject 1: "))
mark2 = int(input("Enter your subject 2: "))
mark3 = int(input("Enter your subject 3: "))
mark4 = int(input("Enter your subject 4: "))

total = mark1 + mark2 + mark3 + mark4
percentage = total / 4

print("\nstudent name: ", name)
print("total :", total)
print("percentage ;", percentage)


if percentage>= 80:
    print("Grade A+")
elif percentage >= 70:
    print("Grade B")
elif percentage >= 60:
    print("Grade C")
elif percentage >= 50:
    print("Grade D")
else:
    print("Fail")

