str = input()

max_count = 0
most_freq = ""

for i in range(len(str)):
    current = str.count(str[i])
    # Если текущий символ встречается не реже, чем максимальный найденный ранее, обновляем максимум и запоминаем символ
    if current >= max_count:
        max_count = current
        most_freq = str[i]

print(most_freq)