import random

def generate_lottery_ticket():
    numbers = sorted(random.sample(range(1, 50), 7))
    return ' '.join([str(number) for number in numbers])


print(generate_lottery_ticket())