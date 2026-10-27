from math import sin, cos, tan, radians

x_degree = float(input())
x = radians(x_degree)
result = sin(x) + cos(x) + pow(tan(x), 2)

print(result)