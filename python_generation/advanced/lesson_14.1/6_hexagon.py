import turtle

def hexagon(side):
    turtle.shape("turtle")
    for _ in range(6):
        turtle.forward(side)
        turtle.right(60)


a = int(input())
for _ in range(6):
    hexagon(a)
    turtle.forward(a)
    turtle.left(60)
turtle.done()