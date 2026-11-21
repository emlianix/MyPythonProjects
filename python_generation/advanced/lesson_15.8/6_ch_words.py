filtered = filter(lambda w: len(w) == 6, words)
print(*sorted(filtered))