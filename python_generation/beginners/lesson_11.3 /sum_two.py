n = int(input())
digits = []

for _ in range(n):
	num = int(input())
	digits.append(num)

digits_new = []
for i in range(len(digits) - 1):
	digits_new.append(digits[i] + digits[i + 1])
	 
print(digits_new)