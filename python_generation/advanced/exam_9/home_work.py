n = int(input())
m = int(input())
k = int(input())
p = int(input())

# Количество учеников, у которых возникли проблемы (объединение множеств)
students_with_issues = m + k - p
# Количество учеников, которые выполнили домашнее задание
completed_homework = n - students_with_issues

print(completed_homework)