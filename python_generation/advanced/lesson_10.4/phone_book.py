n = int(input())
book = {}
for _ in range(n):
    phone, name = input().split()
    book.setdefault(name.lower(), []).append(phone)

m = int(input())
for _ in range(m):
    query = input().lower()
    if query in book:
        print(*book[query])
    else:
        print("абонент не найден")