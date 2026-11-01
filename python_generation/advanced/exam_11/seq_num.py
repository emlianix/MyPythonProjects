words = input().split()
counts = {}
result = []

for word in words:
    counts[word] = counts.get(word, 0) + 1
    result.append(counts[word])

print(*result)