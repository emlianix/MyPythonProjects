import turtle

def triangle(side):
    turtle.shape('turtle')
    turtle.right(60)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)
    turtle.right(120)
    turtle.forward(side)


a = int(input())
triangle(a)