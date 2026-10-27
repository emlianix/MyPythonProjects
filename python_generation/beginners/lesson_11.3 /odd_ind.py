num = []
for _ in range(int(input())):
	num.append(int(input()))

del num[1::2]
	
print(num)