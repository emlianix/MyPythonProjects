from turtle import *

def triangle(side):
    hideturtle()
    pensize(2)
    for _ in range(3):
        forward(side)
        left(120)


a = int(input())
triangle(a)
penup()
goto(0, a*0.6)
pendown()
right(60)
triangle(a)
done()