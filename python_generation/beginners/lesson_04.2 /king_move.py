x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x1 - x2
dy = y1 - y2

if -1 <= dx <= 1 and -1 <= dy <= 1:
    print("YES")
else:
    print("NO")