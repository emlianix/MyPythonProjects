n, m = [int(n) for n in input().split()]

# Создаём матрицу с чередованием символов по сумме индексов (i + j)
board = [["." if (i + j) % 2 == 0 else "*" for j in range(m)] for i in range(n)]

for row in board:
    print(*row)