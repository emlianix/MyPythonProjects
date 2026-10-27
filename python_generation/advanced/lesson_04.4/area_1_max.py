def input_sq_matrix(size):
	matrix = []
	for _  in range(size):
		row = [int(num) for num in input().split()]
		matrix.append(row)
	return matrix
	

n = int(input())
mtrx = input_sq_matrix(n)
temp = []

for i in range(n):
    for j in range(n):
        if j <= i and j <= n - 1 - i or j >= i and j >= n - 1 - i:
        	temp.append(mtrx[i][j])

print(max(temp))