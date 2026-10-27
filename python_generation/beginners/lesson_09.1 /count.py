s = input()
n = 0
m = 0

for c in s:
	if c == "+":
		n += 1
	if c == "*":
		m += 1

print(f"Символ + встречается {n} раз")
print(f"Символ * встречается {m} раз")