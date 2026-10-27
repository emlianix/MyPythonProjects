a, b = int(input()), int(input())

for i in range(a, b + 1):
	if i > 1:
		is_prime = True
		for d in range(2, int(i**0.5) + 1):
			if i % d == 0:
				is_prime = False
				break
		if is_prime:
			print(i)