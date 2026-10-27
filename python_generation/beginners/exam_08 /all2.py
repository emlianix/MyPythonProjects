n = int(input())
cnt_3 = 0
cnt_last = 0
last_digit = n % 10
cnt_even = 0
sum_5 = 0
prod_7 = 1
cnt_05 = 0

while n > 0:
	last = n % 10
	if last == 3:
		cnt_3 += 1
	if last == last_digit:
		cnt_last += 1
	if last % 2 == 0:
		cnt_even += 1
	if last > 5:
		sum_5 += last
	if last > 7:
		prod_7 *= last
	if last == 0 or last == 5:
		cnt_05 += 1
	n //= 10
	
print(cnt_3)
print(cnt_last)
print(cnt_even)
print(sum_5)
print(prod_7)
print(cnt_05)