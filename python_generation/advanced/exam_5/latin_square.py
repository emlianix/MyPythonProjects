n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

is_latin = True

for k in range(1, n + 1):
    for i in range(n):
        # считаем, сколько раз число k встречается в строке i и в столбце i
        in_row = 0
        in_col = 0
        for j in range(n):
            if matrix[i][j] == k:
                in_row += 1
            if matrix[j][i] == k:
                in_col += 1
        if in_row != 1 or in_col != 1:
            is_latin = False

print("YES" if is_latin else "NO")