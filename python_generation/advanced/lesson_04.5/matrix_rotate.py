n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

# 1. Транспонирование матрицы
for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# 2. Реверс каждой строки
for i in range(n):
    matrix[i].reverse()

for row in matrix:
    print(*row)