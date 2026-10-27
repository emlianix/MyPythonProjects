from math import sqrt

a = int(input())
b = int(input())

sum = a + b
diff = a - b
prod = a * b
div = a / b
integer = a // b
rem = a % b
sqr = sqrt(a**10 + b**10)

print(sum, diff, prod, div, integer, rem, sqr, sep="\n")