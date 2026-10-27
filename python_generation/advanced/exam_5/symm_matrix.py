n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

is_symmetric = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - 1 - j][n - 1 - i]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

print("YES" if is_symmetric else "NO")