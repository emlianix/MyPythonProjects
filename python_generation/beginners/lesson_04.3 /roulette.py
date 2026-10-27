n = int(input())

if not (0 <= n <= 36):
    print("ошибка ввода")
elif n == 0:
    print("зеленый")
elif (1 <= n <= 10) or (19 <= n <= 28):
    if n % 2 == 0:
        print("черный")
    else:
        print("красный")
else:  # Сюда автоматически попадают диапазоны 11–18 и 29–36
    if n % 2 == 0:
        print("красный")
    else:
        print("черный")