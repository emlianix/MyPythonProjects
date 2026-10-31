def count_letters(word):
    counts = {}
    for ch in word:
        counts[ch] = counts.get(ch, 0) + 1
    return counts


a = input().lower()
b = input().lower()

print('YES' if count_letters(a) == count_letters(b) else 'NO')