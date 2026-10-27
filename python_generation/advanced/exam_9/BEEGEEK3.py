m = int(input())
n = int(input())
# Создаём множества с фамилиями учеников
math_students = {input() for _ in range(m)}
cs_students = {input() for _ in range(n)}

# Находим учеников, изучающих только один предмет (симметрическая разность)
only_one = math_students ^ cs_students

# Выводим результат
if len(only_one) == 0:
    print("NO")
else:
    print(len(only_one))