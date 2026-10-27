n, m = [int(x) for x in input().split()]
matrix = [[0] * m for _ in range(n)]

# Заполняем по столбцам
count = 1
for j in range(m):
    for i in range(n):
        matrix[i][j] = count
        count += 1

for row in matrix:
	print("".join(str(x).ljust(3) for x in row))