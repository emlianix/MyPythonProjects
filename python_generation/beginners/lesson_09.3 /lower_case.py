s = input()
cnt = 0

for char in s:
	if char == char.lower() and char not in "0123456789+-%$":
		cnt += 1

print(cnt)