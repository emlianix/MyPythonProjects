def distance_sqr(p):
    x, y = p
    return x**2 + y**2

print(sorted(points, key=distance_sqr))