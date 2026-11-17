def is_valid(x):
    return 10 <= abs(x) <= 99 and x % 7 == 0

def square(x):
    return x**2

print(sum(map(square, filter(is_valid, numbers))))