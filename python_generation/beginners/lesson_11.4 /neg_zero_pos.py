num = []
for _ in range(int(input())):
	num.append(int(input()))

neg = []
zero = []
pos = []

for n in num:
	if n < 0:
		neg.append(n)
	elif n == 0:
		zero.append(n)
	else:
		pos.append(n)
		
print(*neg, *zero, *pos, sep='\n')