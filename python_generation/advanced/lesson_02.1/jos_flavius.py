n = int(input())
k = int(input())

survivor = 0  # Для 1 человека позиция (0-indexed) равна 0

for i in range(2, n + 1):
    survivor = (survivor + k) % i

print(survivor + 1)  # Переводим в 1-based нумерацию