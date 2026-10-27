from math import pi, sin

d1, d2, alpha = map(int, input().split())

rad = alpha / 180 * pi
square = round((d1 * d2 / 2) * sin(rad), 1)