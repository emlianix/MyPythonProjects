def print_digit_sum(num):
    digit_sum = 0
    while num > 0:
    	digit_sum += num % 10
    	num //= 10
    	
    print(digit_sum)


n = int(input())

print_digit_sum(n)