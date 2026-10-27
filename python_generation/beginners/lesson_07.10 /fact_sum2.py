n = int(input())
total_sum = 0

for i in range(1, n + 1):
    factorial = 1
    
    # Вложенный цикл считает факториал для текущего числа i (i!)
    for j in range(1, i + 1):
        factorial *= j
    total_sum += factorial

print(total_sum)