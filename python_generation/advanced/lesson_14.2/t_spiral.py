from turtle import *

shape('turtle')
pensize(3)
Screen().bgcolor('PaleGreen2')
penup()
a = 1

for i in range(50):
    stamp()
    right(25)
    forward(a + i)

done()