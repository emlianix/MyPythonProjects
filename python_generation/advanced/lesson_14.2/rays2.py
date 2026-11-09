from turtle import *

Screen().colormode(255)
penup()
goto(0,200)
pensize(2)

for i in range(-400, 401, 80):
    pendown()
    color(65, 201, 155)
    goto(i, -200)
    color('blue')
    dot()
    penup()
    goto(0, 200)

color('red')
dot()
hideturtle()
done()