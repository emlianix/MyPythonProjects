n1, n2, n3, n4 = int(input()), int(input()), int(input()), int(input())
min = n1

if n2 < min:
    min = n2
if n3 < min:
    min = n3
if n4 < min:
    min = n4

print(min)