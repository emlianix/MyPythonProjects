def func(num1, num2):
	return num1 % num2 == 0
	
	
n1 = int(input())
n2 = int(input())

if func(n1, n2):
	print("делится")
else:
	print("не делится")