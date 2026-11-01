from random import randint

def coin_flip():
    toss = randint(0, 1)
    return "Решка" if toss == 0 else "Орел"

print(coin_flip())