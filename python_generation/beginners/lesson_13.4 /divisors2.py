def get_factors(num):
	divisors = []
	for i in range(1, num +1):
		if num % i == 0:
			divisors.append(i)
	return divisors
	
def number_of_factors(num):
	return len(get_factors(num))
	
n = int(input())
print(number_of_factors(n))