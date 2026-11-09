from turtle import *

def draw_circle(rad, pos, col):
    penup()
    goto(pos)
    pendown()
    color(col)
    circle(rad)


Screen().colormode(255)
pensize(7)
r = int(input())
p1 = (r, 0)
p2 = (2*r, 1.2*r)
p3 = (0, 1.2*r)
p4 = (-2*r, 1.2*r)
p5 = (-r, 0)
c_green = (0, 249, 0)
c_blue = (0, 202, 255)

draw_circle(r, p1, c_green)
draw_circle(r, p2, 'red')
draw_circle(r, p3, 'black')
draw_circle(r, p4, c_blue)
draw_circle(r, p5, 'yellow')

done()