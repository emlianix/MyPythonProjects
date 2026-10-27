text = input()

first_idx = text.find('h')
last_idx = text.rfind('h')
sub = text[first_idx + 1:last_idx]
rev_sub = sub[::-1]

print(text[:first_idx + 1] + rev_sub + text[last_idx:])