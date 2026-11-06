from fractions import Fraction as F
from math import gcd

n = int(input())

for a in range((n - 1) // 2, 0, -1):
    b = n - a
    if gcd(a, b) == 1:
        print(F(a, b))
        break