# positional only parametres
def add(a, b, /, c, d=10):
    return a + b + c + d
    


sum = add(5, 2, 3, 4)
print(sum)

