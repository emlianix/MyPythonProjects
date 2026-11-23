from random import choice

def get_random_string(filename):
    file = open(filename)
    lines = list(map(str.strip, file.readlines()))
    rand_line = choice(lines)
    file.close()
    return rand_line