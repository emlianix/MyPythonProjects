n = int(input())
current = 1

for i in range(1, n + 1):
	for _ in range(i):
		print(current, end=" ")
		current += 1
	print()