import turtle

def rombe(side):
    for _ in range(2):
        turtle.forward(side)
        turtle.left(120)
        turtle.forward(side)
        turtle.left(60)


a = int(input())
turtle.shape("turtle")
rombe(a)
turtle.done()