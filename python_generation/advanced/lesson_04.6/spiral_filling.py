n, m = map(int, input().split())

matrix = [[0] * m for _ in range(n)]
# Задаём начальные границы
top, bottom = 0, n - 1
left, right = 0, m - 1
num = 1  # текущее число для записи

while num <= n * m:
    # 1. Движение влево -> вправо по верхней строке
    for col in range(left, right + 1):
        if num > n * m:
            break
        matrix[top][col] = num
        num += 1
    top += 1

    # 2. Движение сверху -> вниз по правому столбцу
    for row in range(top, bottom + 1):
        if num > n * m:
            break
        matrix[row][right] = num
        num += 1
    right -= 1

    # 3. Движение справа -> влево по нижней строке
    for col in range(right, left - 1, -1):
        if num > n * m:
            break
        matrix[bottom][col] = num
        num += 1
    bottom -= 1

    # 4. Движение снизу -> вверх по левому столбцу
    for row in range(bottom, top - 1, -1):
        if num > n * m:
            break
        matrix[row][left] = num
        num += 1
    left += 1

for row in matrix:
	print("".join(str(x).ljust(3) for x in row))