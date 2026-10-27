n = int(input())
total_sum = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i  # вычисляем i! на основе (i-1)!
    total_sum += factorial  # прибавляем текущий факториал к общей сумме

print(total_sum)