m = int(input())
n = int(input())
# Считываем фамилии учеников, изучающих математику
math_students = {input() for _ in range(m)}
# Считываем фамилии учеников, изучающих информатику
cs_students = {input() for _ in range(n)}

# Находим учеников, которые изучают только математику (разность множеств)
only_math = math_students - cs_students

# Выводим их количество
print(len(only_math))