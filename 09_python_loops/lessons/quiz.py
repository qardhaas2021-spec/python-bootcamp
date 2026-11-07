# Keep asking until user gives a valid answer (A, B, C, or D)
while True:
    user_answer = input("Your answer (A/B/C/D): ").upper()
    if user_answer in ["A", "B", "C", "D"]:
        break   # Valid answer! Exit the while loop
        print("⚠️  Please type only A, B, C, or D!")
