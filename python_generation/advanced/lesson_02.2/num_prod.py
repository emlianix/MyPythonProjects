n = int(input())
num = [int(input()) for _ in range(n)]
x = int(input())
is_prod = False

for i in range(len(num)):
	for j in range(i + 1, len(num)):
		if num[i] * num[j] == x:
			is_prod = True
			break
	if is_prod:
		break
			
if is_prod:
	print("ДА")
else:
	print("НЕТ")