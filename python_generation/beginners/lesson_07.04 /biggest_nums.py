n = int(input())
max1 = 0
max2 = 0

for _ in range(n):
	num = int(input())
	if num > max1:
		max2 = max1  # старый максимум становится вторым
		max1 = num  # записываем новый самый большой
	elif num > max2:
		max_num2 = num  # обновляем только второй максимум

print(max1)
print(max2)