from math import sqrt, sin

def square(x):
    return x**2

def cube(x):
    return x**3

n = int(input())
name = input()

funcs = {
    'квадрат': square,
    'куб': cube,
    'корень': sqrt,
    'модуль': abs,
    'синус': sin
}

print(funcs[name](n))