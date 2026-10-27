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
    
print()
for i in range(m):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()