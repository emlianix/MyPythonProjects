n = int(input())
count = 0

while n > 0:
    if n >= 25:
        n -= 25
    elif n >= 10:
        n -= 10
    elif n >= 5:
        n -= 5
    else:
        n -= 1
    count += 1

print(count)