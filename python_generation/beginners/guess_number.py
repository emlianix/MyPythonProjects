import random

number = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')

def is_valid(num):
	if num.isdigit() and 1 <= int(num) <= 100:
		return True
	else:
		return False
		
count = 0
while True:
	guess = input('Введите целое число от 1 до 100: ')
	if is_valid(guess):
		guess = int(guess)
		if guess > number:
			print('Ваше число больше загаданного, попробуйте ещё раз')
			count += 1
		elif guess < number:
			print('Ваше число меньше загаданного, попробуйте ещё раз')
			count += 1
		else:
			print('Вы угадали, поздравляем!')
			count += 1
			break
	else:
		print('А может быть всё-таки введём целое число от 1 до 100?')

print(f'Количество попыток: {count}')
print('Спасибо, что играли в числовую угадайку. Ещё увидимся...')