set1 = {int(x) for x in input().split()}
set2 = {int(x) for x in input().split()}
# Находим пересечение (общие числа)
common_numbers = set1 & set2

if common_numbers:
  # Сортируем по убыванию и выводим через пробел
  print(*sorted(common_numbers, reverse=True))
else:
  print("BAD DAY")