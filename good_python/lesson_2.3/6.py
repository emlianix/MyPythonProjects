from math import factorial

n, k = map(int, input().split())

Cnk = factorial(n) / (factorial(k) * factorial(n - k))

print(int(Cnk))