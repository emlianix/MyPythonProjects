import turtle

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)


turtle.shape("turtle")
turtle.setheading(75)
square()
