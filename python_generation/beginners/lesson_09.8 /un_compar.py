s1 = input()
s2 = input()

s1_c = ""
for char in s1:
    if char.isalpha():
        s1_c += char.lower()

s2_c = ""
for char in s2:
    if char.isalpha():
        s2_c += char.lower()

if s1_c == s2_c:
    print("YES")
else:
    print("NO")