num = int(input())

d1 = num // 100
d2 = (num//10) % 10
d3 = num % 10

print(f"Сумма цифр = {d1 + d2 + d3}")
print(f"Произведение цифр = {d1 * d2 * d3}")