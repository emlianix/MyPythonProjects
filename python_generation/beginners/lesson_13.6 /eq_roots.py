from math import sqrt

# объявление функции
def solve(a, b, c):
    d = b**2 - 4*a*c
    if d == 0:
    	x = -(b / (2*a))
    	return x, x
    elif d > 0:
    	x = (-b - sqrt(d)) / (2 * a)
    	y = (-b + sqrt(d)) / (2 * a)
    	if x < y:
    		return x, y
    	else:
    		return y, x


# считываем данные
n1, n2, n3 = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(n1, n2, n3)
print(x1, x2)