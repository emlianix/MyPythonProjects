n = int(input())

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for _ in range(n):
    parts = input().split()
    x = int(parts[0])
    y = int(parts[1])
    
    if x > 0 and y > 0:
        q1 += 1
    elif x < 0 and y > 0:
        q2 += 1
    elif x < 0 and y < 0:
        q3 += 1
    elif x > 0 and y < 0:
        q4 += 1

print(f"Первая четверть: {q1}")
print(f"Вторая четверть: {q2}")
print(f"Третья четверть: {q3}")
print(f"Четвертая четверть: {q4}")