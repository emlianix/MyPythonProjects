a = int(input())
b = int(input())
best_number = a
max_sum = 0

for num in range(a, b + 1):
    current_sum = 0
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            current_sum += i
            # Если делители разные (не случай, когда i * i == num)
            if i != num // i:
                current_sum += num // i

    if current_sum >= max_sum:
        max_sum = current_sum
        best_number = num

print(best_number, max_sum)