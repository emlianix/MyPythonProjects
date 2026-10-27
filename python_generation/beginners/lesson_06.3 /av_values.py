from math import sqrt

a, b = float(input()), float(input())
ar = (a + b) / 2
geom = sqrt(a * b)
harm = 2 * a * b / (a + b)
sq = sqrt((a**2 + b**2) / 2)

print(ar, geom, harm, sq, sep="\n")