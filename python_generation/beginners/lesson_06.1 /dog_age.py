n = float(input())

if n <= 2:
	age = n * 10.5
else:
	age = 2*10.5 + (n-2)*4
	
print(age)