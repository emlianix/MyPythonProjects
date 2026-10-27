numbers = [int(n) for n in input().split()]
# Так как список не пустой, в нём как минимум 1 уникальный элемент
unique_count = 1

for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        unique_count += 1

print(unique_count)