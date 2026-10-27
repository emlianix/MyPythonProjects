import math

a, b, alpha = map(float, input().split())

length_c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(alpha))