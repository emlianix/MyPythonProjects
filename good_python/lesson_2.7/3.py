a, b, c, d, x = map(float, input().split())

res_1 = (a < x < b) or (c <= x <= d)
res_2 = not (a < x < b) and (c <= x <= d)
res_3 = not (a < x < b) and not (c <= x <= d)