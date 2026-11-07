# DEFINING CLASSES AND OBJECTS
class Robot:

    """This class implements a robot"""
    population = 0
    def __init__(self, name, year):
        self.name = name
        self.year = year
        Robot.population += 1

    
    def setEnergy(self, energy):
        self.energy = energy
    
    def __str__(self):
        my_str = f"my name is {self.name} and my price is {self.price}"
        return my_str

    


l1 = Robot("l1", 2023)
l2 = Robot("Ben", 2040)
print(l1.__doc__)
print(f"Robot name:{l1. name}")
print(l1.__doc__)
l1.setEnergy(100)
print(l1.energy)

print(l1.__dict__)
print(Robot.population)
S1 = Robot("marphin", 150)
s2 = Robot("gulen", 50)








class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s1 = Student("Ahmed", 20, 60)
print(s1.name)
print(s1.age)
print(s1.score)


class Student:
    school_name = "macmuur"
    number_of_students = 0

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.number_of_students = Student.number_of_students + 1

    def introduce(self):
        print(f"Hi i am {self.name}, grade{self.grade}, from{self.school_name}")

amina = Student("Amina", 20)
tom = Student("Tom", 30)
print("----instant attributes are privateto each object")
print(amina.name, "|", tom.name)
print(amina.grade, "|", tom.grade)



