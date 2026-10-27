n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    matrix[i][i] = 1  # главная диагональ
    matrix[i][n - 1 - i] = 1  # побочная диагональ

for row in matrix:
	print("".join(str(x).ljust(3) for x in row))