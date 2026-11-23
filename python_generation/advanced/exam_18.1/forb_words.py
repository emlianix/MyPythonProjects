with open(input(), encoding='utf-8') as f:
    text = f.read()
with open(input(), encoding='utf-8') as f:
    banned = f.read().split()

low = text.lower()
chars = list(text)

for word in banned:
    w = word.lower()
    start = low.find(w)
    while start != -1:
        for i in range(start, start + len(w)):
            chars[i] = '*'
        start = low.find(w, start + 1)

print(''.join(chars))