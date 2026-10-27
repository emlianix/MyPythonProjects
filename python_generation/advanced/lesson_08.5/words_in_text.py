s = input().lower()
for ch in ".,;:-?!":
    s = s.replace(ch, "")
print(len(set(s.split())))