n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]

input()

m, k = map(int, input().split())
matrix_b = [list(map(int, input().split())) for _ in range(m)]

# Создание результирующей матрицы размером n x k, заполненной нулями
result = [[0] * k for _ in range(n)]

# Перемножение матриц
for i in range(n):
    for j in range(k):
        for r in range(m):
            result[i][j] += matrix_a[i][r] * matrix_b[r][j]

for row in result:
    print(*row)