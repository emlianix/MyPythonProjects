n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_val = float('-inf')

for i in range(n):
    for j in range(n):
        # Элементы на побочной диагонали и ниже/правее неё
        if i + j >= n - 1:
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]

print(max_val)