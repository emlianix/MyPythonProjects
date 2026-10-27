n = int(input())
last_digit = n % 10  # запоминаем последнюю цифру
all_same = True

while n > 0:
    current_digit = n % 10
    if current_digit != last_digit:
        all_same = False
        break
    n //= 10

if all_same:
    print("YES")
else:
    print("NO")