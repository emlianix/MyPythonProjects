import random

def get_secret_friend(students):
    shuffled = list(students)  # кортеж -> список
    random.shuffle(shuffled)  # случайный порядок по кругу
    n = len(shuffled)

    result = {}
    for i in range(n):
        result[shuffled[i]] = shuffled[(i + 1) % n]  # для последнего ученика n даёт 0, то есть он замыкает круг и получает первого
    return result