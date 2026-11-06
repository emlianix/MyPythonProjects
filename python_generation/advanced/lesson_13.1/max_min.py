from decimal import Decimal as D

d = D(input())
digits = list(d.as_tuple().digits)

if abs(d) < 1:  # the integer part is 0, but as_tuple() doesn't store it
    digits.append(0)
    
print(max(digits) + min(digits))