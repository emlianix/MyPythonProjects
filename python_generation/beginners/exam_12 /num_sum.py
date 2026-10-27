num = [int(n) for n in input().split()]
	
print(*num, sep='+', end='=')
print(sum(num))