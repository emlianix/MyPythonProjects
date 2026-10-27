ip = input().split('.')

for i in ip:
	if not (0 <= int(i) <= 255):
		print('НЕТ')
		break
else:
	print('ДА')