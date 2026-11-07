# in python there are three namespaces and scopes
# 1. the built-in namespaces: python built-in function
# 2. the global(module namespaces): names defined in script
# 3. names defined inside function

t1 = tuple(range(1, 20))
print(t1)

x = 10
def myfunct():
    print(f"x is inside the function {x}")

myfunct()

# GLOBAL = only on this student's desk

school_name = "macmuur school"

def student_desk():
    """local only on this student's desk"""

    pencil = "blue"
    print(f"I study at:", school_name) # can read the board
    print("my pecil is:", pencil)      # only on my desk


student_desk()
print(school_name)


price = 100

def product():
    product_name = "apple"
    print(f"my product name is: {product_name}, and his price is {price}")
    

product()



