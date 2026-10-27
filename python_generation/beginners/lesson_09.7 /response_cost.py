comm = input()
cost = 0

for char in comm:
	cost += ord(char) * 3

print(f"Текст сообщения: '{comm}'")
print(f"Стоимость сообщения: {cost}🐝")