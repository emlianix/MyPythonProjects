s = input().split()
n = int(input())

result = [s[i::n] for i in range(n)]

print(result)