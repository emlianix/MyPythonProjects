n = int(input())
dct = {}
for _ in range(n):
    word, definition = input().split(': ', 1)
    dct[word.lower()] = definition

m = int(input())
for _ in range(m):
    q = input().strip().lower()
    print(dct.get(q, "Не найдено"))