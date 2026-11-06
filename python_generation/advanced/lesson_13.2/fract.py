from fractions import Fraction as F

x, y = input(), input()
print(f"{x} + {y} = {F(x) + F(y)}")
print(f"{x} - {y} = {F(x) - F(y)}")
print(f"{x} * {y} = {F(x) * F(y)}")
print(f"{x} / {y} = {F(x) / F(y)}")