from fractions import Fraction as F
from math import gcd

n = int(input())
result = []

for d in range(2, n + 1):
    for k in range(1, d):
        if gcd(k, d) == 1:
            result.append(F(k, d))

result.sort()

for f in result:
    print(f)