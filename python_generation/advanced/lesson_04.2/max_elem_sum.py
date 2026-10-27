list1 = [int(input()) for i in input().split()]

s = 0
n = 0

for lst in list1:
    s += sum(lst)
    n += len(lst)

print(s / n)