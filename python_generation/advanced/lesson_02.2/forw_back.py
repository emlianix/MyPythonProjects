num = input().split()

for i in range(0, len(num) - 1, 2):
    temp = num[i]
    num[i] = num[i + 1]
    num[i + 1] = temp

print(*num, sep=" ")