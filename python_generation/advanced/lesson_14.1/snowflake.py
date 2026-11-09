import turtle

def rombe(side):
    for _ in range(2):
        turtle.forward(side)
        turtle.left(60)
        turtle.forward(side)
        turtle.left(120)


a = int(input())
turtle.shape("turtle")
turtle.left(18)

for _ in range(10):
    rombe(a)
    turtle.left(36)

turtle.done()