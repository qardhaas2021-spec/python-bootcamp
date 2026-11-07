# BOOLEAN VARIABLES
# A boolean is only True or False

# 1) Create boolean variables
is_logged_in = True
is_locked = False
has_discount = True

print(is_logged_in)   # True
print(is_locked)      # False

# 2) Use them in if / else
if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in.")

# 3) Booleans from comparisons (very common)
age = 20
is_adult = age >= 18          # True
marks = 35
has_passed = marks >= 40      # False

print("Adult?", is_adult)
print("Passed?", has_passed)

if has_passed:
    print("You passed the exam.")
else:
    print("You failed the exam.")

# 4) Truthiness: some values act like False
# False values: False, 0, 0.0, "", [], None
# True values: almost everything else

password = "Ahmed123"
if password:
    print("Password is not empty")
else:
    print("Password is empty")

result = ""
if result:
    print("the result is not empty")
else:
    print("the result is empty")

l1 = [1, 2,]
print(bool(l1))

l2 = 'Ahmed'
print(bool(l2))



