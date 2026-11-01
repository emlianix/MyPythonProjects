n = int(input())
files = {}
for _ in range(n):
    parts = input().split()
    files[parts[0]] = set(parts[1:])

ops = {'read': 'R', 'write': 'W', 'execute': 'X'}

m = int(input())
for _ in range(m):
    op, name = input().split()
    if name in files and ops[op] in files[name]:
        print('OK')
    else:
        print('Access denied')