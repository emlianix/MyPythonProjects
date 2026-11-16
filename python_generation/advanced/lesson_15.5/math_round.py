from decimal import Decimal as D, ROUND_HALF_UP

def math_round(x):
    d = D(str(x)).quantize(D('0.01'), rounding=ROUND_HALF_UP)
    return float(d)

print(*map(math_round, numbers), sep='\n')