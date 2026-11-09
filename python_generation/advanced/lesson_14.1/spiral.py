import turtle

turtle.shape("turtle")
turtle.color("blue")
turtle.speed(2)
n, step = int(input()), int(input())
a = step
turtle.left(90)

for _ in range(n):
    turtle.forward(a)
    turtle.left(90)
    a += step

turtle.done()