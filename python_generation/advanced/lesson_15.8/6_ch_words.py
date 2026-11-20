words = ['justice', 'orange', 'plant', 'sunday']
filtered = list(lambda w: len(w) == 6, words)
result = sorted(filtered)
print(*result)