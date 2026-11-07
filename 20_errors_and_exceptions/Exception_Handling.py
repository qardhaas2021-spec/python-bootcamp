try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a / b
    print(c)

except:
    print("AN ERROR OCCURED")

else:
    print("No Errors")
    print(f"c = {c}")

finally:
    print("Goodbye")
    

x = 10
print(x**x)
print("Some other code")
