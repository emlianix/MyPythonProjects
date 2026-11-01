def count_chars(text):
    dct = {}
    for ch in text.lower():
        if ch.isalnum():
            dct[ch] = dct.get(ch, 0) + 1
    return dct


a = input()
b = input()

print('YES' if count_chars(a) == count_chars(b) else 'NO')