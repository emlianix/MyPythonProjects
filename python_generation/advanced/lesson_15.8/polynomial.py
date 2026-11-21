from functools import reduce

def evaluate(coefficients, x):
    n = len(coefficients)
    terms = map(lambda p: p[1] * x**(n - 1 - p[0]), enumerate(coefficients))
    return reduce(lambda a, b: a + b, terms)


coefficients = list(map(int, input().split()))
x = int(input())
print(evaluate(coefficients, x))