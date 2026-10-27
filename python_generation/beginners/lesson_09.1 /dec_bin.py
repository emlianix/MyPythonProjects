n = int(input())

binary_str = ""

while n > 0:
    remain = n % 2  # остаток от деления на 2 (0 или 1)
    binary_str = str(remain) + binary_str
    n //= 2

print(binary_str)