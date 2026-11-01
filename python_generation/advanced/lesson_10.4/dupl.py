words = input().split()
counts = {}
result = []

for w in words:
    if w in counts:
        result.append(f"{w}_{counts[w]}")
        counts[w] += 1
    else:
        counts[w] = 1
        result.append(w)

print(" ".join(result))