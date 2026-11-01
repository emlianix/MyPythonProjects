n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for row in matrix:
    print(*row)