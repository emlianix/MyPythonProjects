import turtle

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)


a = int(input())
turtle.shape("turtle")
square(a)
turtle.setheading(45)
square(a)
turtle.setheading(90)
square(a)
turtle.setheading(135)
square(a)
turtle.setheading(180)
square(a)
turtle.setheading(225)
square(a)
turtle.setheading(270)
square(a)
turtle.setheading(315)
square(a)