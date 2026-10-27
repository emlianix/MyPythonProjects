num = input().split()
for i in range(len(num)):
	num[i] = int(num[i])

min_idx = num.index(min(num))
max_idx = num.index(max(num))
num[min_idx], num[max_idx] = num[max_idx], num[min_idx]

print(*num)