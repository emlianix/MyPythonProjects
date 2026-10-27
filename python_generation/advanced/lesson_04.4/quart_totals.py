def input_sq_matrix(size):
	matrix = []
	for _  in range(size):
		row = [int(num) for num in input().split()]
		matrix.append(row)
	return matrix
	

n = int(input())
mtrx = input_sq_matrix(n)
qrt1 = 0  # верхняя
qrt2 = 0  # правая
qrt3 = 0  # нижняя
qrt4 = 0  # левая

for i in range(n):
    for j in range(n):
        if i < j and i < n - 1 - j:
            qrt1 += mtrx[i][j]
        elif i < j and i > n - 1 - j:
            qrt2 += mtrx[i][j]
        elif i > j and i > n - 1 - j:
            qrt3 += mtrx[i][j]
        elif i > j and i < n - 1 - j:
            qrt4 += mtrx[i][j]

print("Верхняя четверть:", qrt1)
print("Правая четверть:", qrt2)
print("Нижняя четверть:", qrt3)
print("Левая четверть:", qrt4)