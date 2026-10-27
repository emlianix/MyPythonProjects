s = input()
digits = "0123456789"
cnt = 0

for char in s:
	if char in digits:
		cnt += 1
		
print(cnt)