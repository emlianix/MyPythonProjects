x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Находим разность столбцов (dx)
if x1 > x2:
    dx = x1 - x2
else:
    dx = x2 - x1

# Находим разность строк (dy)
if y1 > y2:
    dy = y1 - y2
else:
    dy = y2 - y1

if dx == 1 and dy == 2:
    print("YES")
elif dx == 2 and dy == 1:
    print("YES")
else:
    print("NO")