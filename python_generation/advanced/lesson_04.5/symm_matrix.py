n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

is_symmetric = True

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

if is_symmetric:
    print("YES")
else:
    print("NO")