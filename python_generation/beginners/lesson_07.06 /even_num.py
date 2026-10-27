n = int(input())

# Находим минимальный делитель, чтобы извлекать цифры слева направо
divider = 1
while n // divider >= 10:
    divider *= 10

i = 0
temp = n

# Идём слева направо, срезая по одной цифре
while divider > 0:
    digit = temp // divider  #первая цифра слева
    
    if digit % 2 == 0:
        i += 1
        print(f"{i}-я четная цифра равна {digit}")
        
    temp %= divider  # оставляем хвост числа
    divider //= 10  # уменьшаем разрядность

if i == 0:
    print("Четных цифр в числе нет")