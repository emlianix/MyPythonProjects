from turtle import *

shape('turtle')
pensize(3)
Screen().bgcolor('DeepSkyBlue')
stamp()

for _ in range(12):
    penup()
    forward(150)
    pendown()
    forward(20)
    penup()
    forward(20)
    stamp()
    backward(190)
    left(30)

done()