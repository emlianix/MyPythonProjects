func = []

for _ in range(int(input())):
	x = int(input())
	f = x**2 + 2*x + 1
	func.append(f)
	print(x)

print()
print(*func, sep='\n')