digit = int(input())
sum_digit = 0

for _ in range(4):
	last = digit % 10
	sum_digit += last
	digit //= 10