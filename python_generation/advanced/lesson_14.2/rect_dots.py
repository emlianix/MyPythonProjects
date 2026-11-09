import turtle

a = int(input())
turtle.shape("turtle")

for _ in range(4):
    turtle.forward(a)
    turtle.dot()
    turtle.left(90)

turtle.done()