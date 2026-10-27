seen = set()
for x in input().split():
    n = int(x)  # убирает ведущие нули
    if n in seen:
        print('YES')
    else:
        print('NO')
        seen.add(n)