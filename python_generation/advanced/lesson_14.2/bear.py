from turtle import *

def circle_at(x, y, r, fill=None):
    """Draw a circle with center (x, y) and radius r."""
    penup()
    goto(x, y - r)  # turtle draws a circle starting from its bottom point
    setheading(0)
    pendown()
    if fill:
        fillcolor(fill)
        begin_fill()
    circle(r)
    if fill:
        end_fill()


pensize(2)
hideturtle()

# Head
circle_at(0, 0, 152)

# Ears
circle_at(-126, 152, 44)
circle_at(122, 155, 44)

# Muzzle
circle_at(0, -65, 88)

# Eyes (filled black)
circle_at(-79, 14, 14, "black")
circle_at(74, 14, 14, "black")

# Nose (white circle)
circle_at(0, -10, 14)

# Line from nose down
penup()
goto(0, -24)
pendown()
goto(0, -113)

done()