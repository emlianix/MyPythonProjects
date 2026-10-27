n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

is_magic = True

# 1. Создаём список из n**2 нулей для отслеживания использованных чисел
used = [0] * (n**2 + 1)

for i in range(n):
    for j in range(n):
        val = matrix[i][j]
        # Если число выходит за пределы от 1 до n**2 или уже встречалось ранее
        if not 1 <= val <= n**2 or used[val] ==1:
            is_magic = False
            break
        used[val] = 1
    if not is_magic:
        break

# Если без повторов, проверяем суммы
# Бёрем сумму первой строки как эталон
if is_magic:
    target_sum = 0
    for j in range(n):
        target_sum += matrix[0][j]

    # 2. Проверяем суммы остальных строк
    for i in range(1, n):
        row_sum = 0
        for j in range(n):
            row_sum += matrix[i][j]
        if row_sum != target_sum:
            is_magic = False
            break

    # 3. Проверяем суммы всех столбцов
    if is_magic:
        for j in range(n):
            col_sum = 0
            for i in range(n):
                col_sum += matrix[i][j]
            if col_sum != target_sum:
                is_magic = False
                break

    # 4. Проверяем суммы диагоналей
    if is_magic:
        main_diag_sum = 0
        sec_diag_sum = 0
        for i in range(n):
            main_diag_sum += matrix[i][i]
            sec_diag_sum += matrix[i][n - 1 - i]

        if main_diag_sum != target_sum or sec_diag_sum != target_sum:
            is_magic = False

if is_magic:
    print("YES")
else:
    print("NO")