sort_words = sorted(data, key=lambda w: (len(w), w))
print(*sort_words)