word = input()
min_w = word
max_w = ""

while word != "КОНЕЦ":
	if word < min_w:
		min_w = word
	elif word > max_w:
		max_w = word
	word = input()

print(f"Минимальная строка ⬇️: {min_w}")
print(f"Максимальная строка ⬆️: {max_w}")