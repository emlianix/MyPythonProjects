def digits_sum(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

num = [int(x) for x in input().split()]
num.sort(key=digits_sum)
print(*num)