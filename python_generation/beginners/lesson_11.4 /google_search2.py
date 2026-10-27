n = int(input())
strings = []
for _ in range(n):
    strings.append(input())

k = int(input())
queries = []
for _ in range(k):
    queries.append(input())

for s in strings:
    s_lower = s.lower()
    found_all = True
    
    for q in queries:
        # Если хотя бы один запрос не нашёлся, строка не подходит
        if q.lower() not in s_lower:
            found_all = False
            break
            
    # Если флаг остался True, значит, все запросы встретились в строке
    if found_all:
        print(s)