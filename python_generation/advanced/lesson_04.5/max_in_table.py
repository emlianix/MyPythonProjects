def input_matrix(rows):
    matrix = [[int(x) for x in input().split()] for _ in range(rows)]
    return matrix
    
    
n = int(input())
m = int(input())
table = input_matrix(n)

max_value = table[0][0]
max_row = 0
max_col = 0

for i in range(n):
    for j in range(m):
        if table[i][j] > max_value:
            max_value = table[i][j]
            max_row = i
            max_col = j

print(max_row, max_col)