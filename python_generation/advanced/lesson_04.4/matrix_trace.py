def input_sq_matrix(size):
	matrix = []
	for _  in range(size):
		temp = [int(num) for num in input().split()]
		matrix.append(temp)
	return matrix
		
	
n = int(input())
mtrx = input_sq_matrix(n)
trace = 0

for i in range(n):
	for j in range(n):
		if i == j:
			trace += mtrx[i][j]
			
print(trace)