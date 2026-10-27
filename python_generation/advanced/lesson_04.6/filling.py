n, m = [int(x) for x in input().split()]

# Для строки j и столбца i значение равно j * m + i + 1
matrix = [[j * m + i + 1 for i in range(m)] for j in range(n)]

for row in matrix:
	print("".join(str(x).ljust(3) for x in row))