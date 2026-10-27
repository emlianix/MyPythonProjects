n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        # Условие попадания в верхний или нижний треугольник
        if (i <= j and i + j <= n - 1) or (i >= j and i + j >= n - 1):
            matrix[i][j] = 1
            
for row in matrix:
	print("".join(str(x).ljust(3) for x in row))