import random
import string

def generate_password(length):
    excluded = "lI1oO0"
    symbols = [
        char for char in (string.ascii_letters + string.digits)
        if char not in excluded
    ]
    return "".join(random.choice(symbols) for _ in range(length))

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n = int(input())
m = int(input())

print(*generate_passwords(n, m), sep="\n")