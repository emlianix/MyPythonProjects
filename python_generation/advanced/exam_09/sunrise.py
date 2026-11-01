data = input().split()
# Общее количество показаний
total_count = len(data)
# Количество уникальных показаний (множество удаляет дубликаты)
unique_count = len(set(data))
# Максимальное количество элементов для удаления
max_removed = total_count - unique_count

print(max_removed)