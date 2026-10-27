n = int(input())
d1 = n // 100
d2 = n // 10 % 10
d3 = n % 10

max_digit = max(d1, d2, d3)
min_digit = min(d1, d2, d3)
mid_digit = (d1 + d2 + d3) - max_digit - min_digit
	
if (max_digit - min_digit) == mid_digit:
	print("Число интересное")
else:
	print("Число неинтересное")