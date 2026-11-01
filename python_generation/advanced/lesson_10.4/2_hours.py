def to_minutes(time):
    parts = time.split(':')
    return int(parts[0]) * 60 + int(parts[1])


n = int(input())
entry = {}
for _ in range(n):
    car_id, t = input().split(': ')
    entry[car_id] = to_minutes(t)

m = int(input())
for _ in range(m):
    car_id, t = input().split(': ')
    duration = (to_minutes(t) - entry[car_id]) % 1440
    if duration > 120:
        print(f'{car_id}: {(duration - 120) * 3}₽')
    else:
        print(f'{car_id}: плата не взимается')