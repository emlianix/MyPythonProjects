import random

def generate_password(length):
    password = ''
    for _ in range(length):
        # Случайно выбираем: заглавная или строчная буква
        if random.choice([True, False]):
            password += chr(random.randint(65, 90))    # A..Z
        else:
            password += chr(random.randint(97, 122))   # a..z
    return password

print(generate_password(int(input())))