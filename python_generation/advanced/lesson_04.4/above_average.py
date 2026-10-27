from statistics import mean

def input_sq_matrix(size):
	matrix = []
	for _  in range(size):
		temp = [int(num) for num in input().split()]
		matrix.append(temp)
	return matrix
	
	
n = int(input())
mtrx = input_sq_matrix(n)

for i in range(n):
	row_count = 0
	for j in range(n):
		if mtrx[i][j] > mean(mtrx[i]):
			row_count += 1
	print(row_count)