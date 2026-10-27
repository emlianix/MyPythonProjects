n, m = [int(x) for x in input().split()]

for i in range(n):
    row = [str((i + j) % m + 1).ljust(3) for j in range(m)]
    print("".join(row))