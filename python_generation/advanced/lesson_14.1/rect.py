import turtle

def rectangle(width, height):
    turtle.shape('turtle')
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)


a, b = int(input()), int(input())
rectangle(a, b)