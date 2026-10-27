n = int(input())
m = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

i, j = input().split()
i = int(i)
j = int(j)

for row in matrix:
    row[i], row[j] = row[j], row[i]
    
for row in matrix:
	print(*row)