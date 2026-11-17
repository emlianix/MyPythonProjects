# Based on Skulpt (https://github.com/skulpt/skulpt)
# Approximately corresponds Python 3.6

from turtle import *

bgcolor('black')
colors = ['red','orange','yellow','green','blue','indigo','violet']
speed(0)

for i in range(400):
    color(colors[i % len(colors)])
    width(i / 10)
    forward(i)
    right(61)
