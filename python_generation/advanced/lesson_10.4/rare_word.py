text = input().lower()

for ch in '.,!?:;-':
    text = text.replace(ch, ' ')

words = text.split()
counts = {}

for w in words:
    counts[w] = counts.get(w, 0) + 1

min_count = min(counts.values())
print(min(w for w, c in counts.items() if c == min_count))