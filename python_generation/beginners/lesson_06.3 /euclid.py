from math import sqrt, pow

x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
p = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

print(p)