from turtle import *

colors = ["red", "blue", "yellow", "green", "purple", "orange"]
j = 0

for i in range(1, 46):
    color(colors[j])
    pensize(i)
    forward(i * 5)
    left(45)
    if j == 5:
        j = 0
    else:
        j += 1
        
done()