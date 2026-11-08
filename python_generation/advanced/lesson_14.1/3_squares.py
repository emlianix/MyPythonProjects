import turtle

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)


a = int(input())
turtle.shape("turtle")
turtle.setheading(75)
square(a)
turtle.setheading(50)
square(a)
turtle.setheading(25)
square(a)