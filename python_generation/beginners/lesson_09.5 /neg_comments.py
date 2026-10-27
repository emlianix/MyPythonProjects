n = int(input())

for i in range(n):
	c = input()
	if c.isspace() or c == "":
		print(f"{i + 1}: COMMENT SHOULD BE DELETED")
	else:
		print(f"{i + 1}: {c}")