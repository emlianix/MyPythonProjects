from turtle import *
from time import sleep

R = 120            # moon radius
SKY = "#0a2dff"    # background color
MOON = "#ffaa00"   # moon color

def disk(x, y, r, col):
    """Filled circle centered at (x, y)."""
    penup()
    goto(x, y - r)   # circle() starts drawing from the bottom point
    setheading(0)
    color(col)
    begin_fill()
    circle(r)
    end_fill()

setup(600, 600)
bgcolor(SKY)
title("Moon phases")
hideturtle()
tracer(0)

step = 4
# the shadow moves right -> left: first it uncovers the moon (0 -> -2R),
# then comes back from the right side and covers it again (2R -> 0)
offsets = list(range(0, -2 * R - 1, -step)) + list(range(2 * R, -1, -step))

while True:
    for dx in offsets:
        clear()
        disk(0, 0, R, MOON)    # moon
        disk(dx, 0, R, SKY)    # shadow in the sky color
        update()
        sleep(0.03)
    sleep(0.5)