n = int(input()[1:])  # убираем '#', используя срез

for _ in range(n):
    line = input()

    if '#' in line:  # если есть комментарий, отсекаем его
        line = line.split('#', 1)[0]
    
    print(line.rstrip())