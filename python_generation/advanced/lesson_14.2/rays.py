from turtle import *

n = int(input())
pensize(3)

for _ in range(n):
    forward(100)
    stamp()
    backward(100)
    left(360/n)

done()