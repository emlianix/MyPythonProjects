import random

def generate_password(pass_length, pass_chars):
	password = ''
	for _ in range(pass_length):
		password += random.choice(pass_chars)
	return password

	
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

n = int(input('Enter the number of passwords to generate: '))
length = int(input('Password length: '))
dig = input('Include digits? y/n ')
uppercase = input('Include uppercase letters? y/n ')
lowercase = input('Include lowercase letters? y/n ')
punct = input('Include punctuation? y/n ')
ambiguous = input('Exclude ambiguous characters (il1Lo0O)? y/n ')

if dig == 'y':
	chars += digits
if uppercase == 'y':
	chars += uppercase_letters
if lowercase == 'y':
	chars += lowercase_letters
if punct == 'y':
	chars += punctuation
if ambiguous == 'y':
	for ch in 'il1Lo0O':
		if ch in chars:
			chars = chars.replace(ch, '')
				
for _ in range(n):
	print(*generate_password(length, chars), sep='')