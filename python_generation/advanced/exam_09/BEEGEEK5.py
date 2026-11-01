m = int(input())
n = int(input())
seen = set()
both = set()

for _ in range(m + n):
    surname = input()
    if surname in seen:
        both.add(surname)
    else:
        seen.add(surname)

result = len(seen) - len(both)

if result == 0:
    print('NO')
else:
    print(result)