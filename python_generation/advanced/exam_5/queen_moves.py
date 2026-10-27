board = [["."] * 8 for _ in range(8)]
pos = input()

# Переводим координаты в индексы матрицы
c = ord(pos[0]) - ord('a')
r = 8 - int(pos[1])
# Ставим ферзя
board[r][c] = "Q"

# Все возможные ходы ферзя
moves = []
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
for dr, dc in directions:
    for k in range(1, 8):
        moves.append((dr * k, dc * k))

# Отмечаем клетки, которые бьёт ферзь
for move in moves:
    nr = r + move[0]
    nc = c + move[1]
    # Проверяем, не выходят ли новые индексы за пределы доски 8x8
    if 0 <= nr < 8 and 0 <= nc < 8:
        board[nr][nc] = "*"

for row in board:
	print(*row)