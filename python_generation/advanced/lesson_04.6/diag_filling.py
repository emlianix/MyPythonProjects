n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]
count = 1

# k — сумма индексов (i + j) для текущей диагонали
for k in range(n + m - 1):
    for i in range(n):
        j = k - i
        if 0 <= j < m:
            matrix[i][j] = count
            count += 1

for row in matrix:
	print("".join(str(x).ljust(3) for x in row))