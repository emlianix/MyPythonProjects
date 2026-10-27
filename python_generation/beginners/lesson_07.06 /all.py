n = int(input())
# Save original n to calculate the first digit later
original_n = n
# Grab the last digit right away
last = n % 10
sum_digits = 0
count = 0
prod = 1

# Process digits from right to left
while n > 0:
    current_digit = n % 10
    sum_digits += current_digit
    count += 1
    prod *= current_digit
    n = n // 10
    
# Calculate first digit and sum after the loop
first = original_n // 10 ** (count - 1)
arith_mean = sum_digits / count
sum_1_2 = first + last

print(sum_digits, count, prod, arith_mean, first, sum_1_2, sep="\n")