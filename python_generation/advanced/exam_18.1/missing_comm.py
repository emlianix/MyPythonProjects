with open(input(), encoding='utf-8') as f:
    lines = f.read().splitlines()

missing = []
for i, line in enumerate(lines):
    if line.startswith('def '):
        name = line[4:].split('(')[0].strip()
        if i == 0 or not lines[i - 1].startswith('#'):
            missing.append(name)

if missing:
    print(*missing, sep='\n')
else:
    print('Best Programming Team')