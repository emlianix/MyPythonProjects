from math import factorial

# объявление функции
def compute_binom(n, k):
    x = factorial(n) / (factorial(k) * factorial(n - k))
    return int(x)

# считываем данные
a = int(input())
b = int(input())

# вызываем функцию
print(compute_binom(a, b))