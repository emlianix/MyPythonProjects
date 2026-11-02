import random
import string

def generate_index():
    letters = string.ascii_uppercase
    return (
        random.choice(letters)
        + random.choice(letters)
        + str(random.randint(0, 99))
        + '_'
        + str(random.randint(0, 99))
        + random.choice(letters)
        + random.choice(letters)
    )

print(generate_index())