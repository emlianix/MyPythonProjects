from turtle import *
from random import randint

Screen().colormode(255)

for i in range(1, 400):
    speed(0)
    pencolor(randint(1,255),randint(1,255),randint(1,255))
    circle(1 * i)
    right(90)

done()