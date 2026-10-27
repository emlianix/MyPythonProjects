n = int(input())
mid = (n+1) // 2

for i in range(1, mid + 1):
	for j in range(i):
		print("*", end="")
	print()
	
for i in range(mid - 1, 0, -1):
	for j in range(i):
		print("*", end="")
	print()