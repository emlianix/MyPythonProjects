L = [int(x) for x in input().split()]
M = [int(x) for x in input().split()]
result = [L[i] + M[i] for i in range(len(L))]

print(*result)