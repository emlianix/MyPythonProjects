num =[]
for _ in range(int(input())):
	num.append(int(input()))

# 1. Находим индексы мин. и макс. за один проход
min_idx = 0
max_idx = 0

for i in range(1, len(num)):
    if num[i] < num[min_idx]:
        min_idx = i
    if num[i] > num[max_idx]:
        max_idx = i

# 2. Идём от последнего индекса до первого с шагом -1
for i in range(len(num) - 1, -1, -1):
    if i == min_idx or i == max_idx:
        del num[i]

print(*num, sep='\n')