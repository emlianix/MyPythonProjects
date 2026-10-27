n = int(input())
is_ordered = True

while n >= 10:
    last = n % 10
    prev = n % 100 // 10
    # Если last > prev, значит последовательность нарушена
    if last > prev:
        is_ordered = False
        break
    n //= 10

if is_ordered:
    print("YES")
else:
    print("NO")