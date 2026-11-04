import random
import string

def generate_password(length):
    password = ''
    for _ in range(length):
        password += random.choice(string.ascii_letters)
    return password