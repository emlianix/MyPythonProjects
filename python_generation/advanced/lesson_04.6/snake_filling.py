n, m = map(int, input().split())

matrix = [[0] * m for _ in range(n)]
num = 1

for i in range(n):
    if i % 2 == 0:
        # Чётная строка: заполняем слева направо
        for j in range(m):
            matrix[i][j] = num
            num += 1
    else:
        # Нечётная строка: заполняем справа налево
        for j in range(m - 1, -1, -1):
            matrix[i][j] = num
            num += 1

for row in matrix:
	print("".join(str(x).ljust(3) for x in row))