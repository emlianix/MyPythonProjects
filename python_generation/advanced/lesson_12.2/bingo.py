from random import sample

def generate_bingo():
    numbers = sample(range(1, 76), 24)
    numbers.insert(12, 0)
    board = [numbers[i:i+5] for i in range(0, 25, 5)]
    return board

print(generate_bingo())