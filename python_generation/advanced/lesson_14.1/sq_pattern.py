import turtle

def square(side):
    for _ in range(4):
        turtle.forward(side)
        turtle.right(90)


a, step, n = int(input()), int(input()), int(input())
turtle.shape("turtle")
turtle.speed(2)
turtle.right(180)

for _ in range(n):
    square(a)
    a += step

turtle.done()