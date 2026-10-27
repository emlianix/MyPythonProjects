str = []
n = int(input())
for _ in range(n):
	str.append(input())

search = input().lower()

for s in str:
	if search in s.lower():
		print(s)