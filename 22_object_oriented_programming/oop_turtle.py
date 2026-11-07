from turtle import Turtle, Screen
my_screen = Screen()
donotello = Turtle()
print(my_screen.canvwidth)
donotello.shape("turtle")
donotello.color('red')
donotello.forward(100)
donotello.right(90)
donotello.forward(100)

my_screen.exitonclick()



class Numbers():
     def __init__(self, a, b):
        self.a = a
        self.b = b

n1 = Numbers(10, 20)
print(n1)
