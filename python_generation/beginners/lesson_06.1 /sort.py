a, b, c = int(input()), int(input()), int(input())

min_digit = min(a, b, c)
max_digit = max(a, b, c)
mid_digit = (a + b + c) - max_digit - min_digit

print(max_digit, mid_digit, min_digit, sep="\n")