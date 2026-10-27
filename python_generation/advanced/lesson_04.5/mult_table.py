n = int(input())
m = int(input())
mult = []

for i in range(n):
	row = []
	for j in range(m):
		row.append(i * j)
	mult.append(row)
	
for r in range(n):
	for c in range(m):
	       print(str(mult[r][c]).ljust(3), end=' ')
	print()