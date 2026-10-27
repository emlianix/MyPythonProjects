n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

result = [row[:] for row in matrix]

for _ in range(m - 1):
    temp = [[0] * n for _ in range(n)]  # для хранения промежуточного результата умножения
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][j] += result[i][k] * matrix[k][j]
    result = temp

for row in result:
    print(*row)