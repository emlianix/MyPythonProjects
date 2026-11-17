def is_valid(n):
    return 100 <= abs(n) <= 999 and n % 5 == 2

def cube(n):
    return n ** 3

    
print(*map(cube, filter(is_valid, numbers)), sep='\n')