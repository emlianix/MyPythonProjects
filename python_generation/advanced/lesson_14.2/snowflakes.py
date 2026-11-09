from turtle import *
from random import randint, uniform

def branch(size):
    # V-shaped twig at the current point
    left(45)
    forward(size)
    backward(size)
    right(90)
    forward(size)
    backward(size)
    left(45)

def snowflake(x, y, size, col):
    penup()
    goto(x, y)
    setheading(90)
    pendown()
    color(col)
    pensize(max(1, size // 40))
    for _ in range(8):       # 8 rays
        forward(size * 0.4)
        branch(size * 0.3)
        forward(size * 0.3)
        branch(size * 0.25)
        forward(size * 0.3)
        branch(size * 0.2)  # fork at the tip
        backward(size)      # return to the center
        right(45)
    penup()


bgcolor("cyan")
hideturtle()

for _ in range(5):
    x = randint(-200, 200)
    y = randint(-200, 200)
    size = randint(30, 120)
    col = (uniform(0, 1), uniform(0, 1), uniform(0, 1))
    snowflake(x, y, size, col)

done()