s = input()
digits = "0123456789"
has_digit = False

for c in s:
	if c in digits:
		has_digit = True
		break
		
if has_digit:
	print("Цифра")
else:
	print("Цифр нет")