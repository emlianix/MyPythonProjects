n = int(input())
m = int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)

for row in matrix:
    print(*row)