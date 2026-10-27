n = int(input())
min_dig = 9
max_dig = 0

while n > 0:
	last_dig = n % 10
	if last_dig < min_dig:
		min_dig = last_dig
	if last_dig > max_dig:
		max_dig = last_dig
	n //= 10
	
print("Максимальная цифра равна", max_dig)
print("Минимальная цифра равна", min_dig)