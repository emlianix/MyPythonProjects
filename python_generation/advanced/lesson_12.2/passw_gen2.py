from random import choice, shuffle
from string import ascii_lowercase, ascii_uppercase, digits

def generate_password(length):
    excluded = "lI1oO0"
    ch_lower, ch_upper, digit = [
        [char for char in source if char not in excluded] 
        for source in (ascii_lowercase, ascii_uppercase, digits)
    ]
    all_sym = ch_lower + ch_upper + digit

    password = [choice(ch_lower), choice(ch_upper), choice(digit)]
    password += [choice(all_sym) for _ in range(length - 3)]
    shuffle(password)

    return "".join(password)

def generate_passwords(count, length):
    return [generate_password(length) for _ in range(count)]


n = int(input())
m = int(input())

print(*generate_passwords(n, m), sep="\n")