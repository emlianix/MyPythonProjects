n = int(input())
letter = "АБВГДЕЖЗИЙКЛМНОП"

for _ in range(n):
	cl = input()
	if (
		len(cl) == 2
		and cl[0].isdigit()
		and cl[1].isalpha()
		and cl[1] in letter
	):
		print("YES")
	else:
		print("NO")