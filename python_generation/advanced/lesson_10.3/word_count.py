counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
max_count = max(counts.values())

print(min(word for word in counts if counts[word] == max_count))