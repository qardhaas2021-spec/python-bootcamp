import random
random.choice
random.sample
dice = random.randint(1, 10)
print(dice)
students = ["Ahmed", "mohamed", "Ali"]
print(random.choice(students))

cards = ["A", "K", "Q", "j"]
random.shuffle(cards)
print(cards)

dice = random.randint(1, 6)
print(f"you rolled a {dice}")

code = random.randint(1000, 9999)
print(f"your code is {code}")

student = ["Ahmed", "Mohamed", "Ali"]
speaker = random.choice(student)
print(f"{speaker} answers the next question")

songs = ["Habibi", "intahi", "desert rose"]
print(f"Now playing: {random.choice(songs)}")

l1 = list("hello")
print(l1)
print(random.choice(l1))

print(random.sample(l1, 4))
