from math import floor

def math_round_to_int(num):
	return floor(num + 0.5)
	
n = float(input())
print(math_round_to_int(n))