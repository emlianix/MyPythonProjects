from turtle import *

shape('turtle')
pensize(3)
penup()
stamp()

for _ in range(10):
    forward(150)
    stamp()
    backward(150)
    left(36)

done()