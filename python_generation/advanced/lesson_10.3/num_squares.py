sqr = {}
for i in range(1, 16):
    sqr.setdefault(i, i**2)

print(sqr)