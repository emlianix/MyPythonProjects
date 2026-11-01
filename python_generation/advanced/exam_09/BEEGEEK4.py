manager_list = input().split()
assistant_list = input().split()

# Объединяем списки в одно множество, чтобы убрать дубликаты
all_students = set(manager_list) | set(assistant_list)
# Сортируем полученные фамилии в лексикографическом порядке
sorted_students = sorted(all_students)

print(*sorted_students)