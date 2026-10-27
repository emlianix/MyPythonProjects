n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

    # Строка элемента на главной диагонали: j
    # Строка элемента на побочной диагонали: n - 1 - j
for j in range(n):
    matrix[j][j], matrix[n - 1 - j][j] = matrix[n - 1 - j][j], matrix[j][j]

for row in matrix:
    print(*row)