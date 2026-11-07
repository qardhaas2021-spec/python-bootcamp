# LOGICAL BOOLEAN OPERATIONS
# Combine True/False values with: and, or, not

# ---------------------------------------------
# 1) and  → True only if BOTH sides are True
# ---------------------------------------------
# True  and True  → True
# True  and False → False
# False and True  → False
# False and False → False

age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter.")
else:
    print("You cannot enter.")

# Real example: login needs correct password AND attempts left
password_ok = True
attempt = 2
if password_ok and attempt > 0:
    print("Login allowed")
else:
    print("Login not allowed")

# ---------------------------------------------
# 2) or  → True if AT LEAST ONE side is True
# ---------------------------------------------
# True  or True  → True
# True  or False → True
# False or True  → True
# False or False → False

is_student = False
is_teacher = True

if is_student or is_teacher:
    print("You can use the school system.")
else:
    print("Access denied.")

# Real example: pass exam with high marks OR bonus
marks = 35
has_bonus = True
if marks >= 40 or has_bonus:
    print("You passed.")
else:
    print("You failed.")

# ---------------------------------------------
# 3) not  → flips True ↔ False
# ---------------------------------------------
# not True  → False
# not False → True

is_locked = False

if not is_locked:
    print("Computer is open. You can use it.")
else:
    print("Computer is locked.")

# ---------------------------------------------
# 4) Combine all three
# ---------------------------------------------
is_logged_in = True
is_admin = False
is_banned = False

# Can edit? logged in, not banned, and (admin OR special case)
can_edit = is_logged_in and not is_banned and (is_admin or True)
print("Can edit?", can_edit)

# ---------------------------------------------
# Quick memory
# ---------------------------------------------
# and = BOTH must be True
# or  = ONE is enough
# not = reverse the answer


age = 20
has_vote = False

if age >= 18 and not has_vote:
    print("you can vote")

password = True
attempts = 3
if password and attempts > 0:
    print("login allowed")
else:
    print("login not allowed")

is_logged_in = True
is_admin = False
is_banned = False

can_edit = is_logged_in and not is_banned and (is_admin or True)
print("Can edit?", can_edit)


has_phone = True
has_lost = False
if has_phone and has_lost:
    print("You can use the phone")
else:
    print("you cannot use the phone")
    

age = 20
has_vote = False
if age >= 18 or has_vote:
    print("you can vote")
else:
    print("you can not vote")

price = 100
discount = False
if price > 100 or discount:
    print("you can buy the product")
else:
    print("you can not buy the product")


marks = 40
has_bonus = True
if marks >= 50 or has_bonus:
    print("you passed the exam")
else:
    print("you failed the exam")
    
    

