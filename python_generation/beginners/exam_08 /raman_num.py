count = 0

for x in range(1, 40000):
    ways = 0
    
    # Вложенные циклы для поиска пар (a, b), где a < b
    for a in range(1, int(x**(1/3)) + 1):
        for b in range(a + 1, int(x**(1/3)) + 1):
            if a**3 + b**3 == x:
                ways += 1
                
    if ways >= 2:
        print(x)
        count += 1
        if count == 5:
            break