n = int(input())
is_sorted = True
prev_surname = ""
prev_title = ""

for _ in range(n):
	book = input()
	surname = book[:book.find(" ")]
	title = book[book.find("«") + 1:-1]
	if surname < prev_surname:
		is_sorted = False
		break
	elif surname == prev_surname:
		if title < prev_title:
			is_sorted = False
			break
	prev_surname = surname
	prev_title = title
	
if is_sorted:
	print("YES")
else:
	print("NO")