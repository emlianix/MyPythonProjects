n = int(input())
common = set(input())
for _ in range(n - 1):
    common &= set(input())

print(*sorted(common))