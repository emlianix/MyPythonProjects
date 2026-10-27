n = int(input())
uniq_str = []

for _ in range(n):
    s = input()
    if s not in uniq_str:
        uniq_str.append(s)

print(*uniq_str, sep='\n')