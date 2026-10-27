char = input()

if char == "Я":
	print("Дальше букв нет")
else:
	print(chr(ord(char) + 1))