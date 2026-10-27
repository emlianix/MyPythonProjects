a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

# Находим левую границу пересечения (наибольшее из a1 и a2)
if a1 > a2:
    left = a1
else:
    left = a2

# Находим правую границу пересечения (наименьшее из b1 и b2)
if b1 < b2:
    right = b1
else:
    right = b2

# Сравниваем границы
if left < right:
    print(left, right)
elif left == right:
    print(left)
else:
    print("пустое множество")