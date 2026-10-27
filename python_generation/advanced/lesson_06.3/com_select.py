n = int(input())
students = []

for _ in range(n):
    surname, grade = input().split()
    students.append((surname, int(grade)))

for surname, grade in students:
    print(surname, grade)
print()
for surname, grade in students:
    if grade >= 4:
        print(surname, grade)