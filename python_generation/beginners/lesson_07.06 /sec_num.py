n = int(input())
orig_n = n
count = 0

while n > 0:
	count += 1
	n //= 10
	
sec_num = orig_n // (10 ** (count - 2)) % 10
print(sec_num)