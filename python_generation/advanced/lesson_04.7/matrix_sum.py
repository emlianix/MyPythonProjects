n, m = map(int, input().split())

matrix1 = [list(map(int, input().split())) for _ in range(n)]

input()

matrix2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    result_row = [matrix1[i][j] + matrix2[i][j] for j in range(m)]
    print(*result_row)