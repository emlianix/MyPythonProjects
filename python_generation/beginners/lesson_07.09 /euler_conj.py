found = False

# Перебираем a <= b <= c <= d, чтобы сократить количество проверок
for a in range(1, 151):
    if found:
        break
    a5 = a ** 5
    
    for b in range(a, 151):
        if found:
            break
        b5 = b ** 5
        
        for c in range(b, 151):
            if found:
                break
            c5 = c ** 5
            
            for d in range(c, 151):
                total = a5 + b5 + c5 + d ** 5
                
                # Подбираем e такое, что e**5 >= total
                # Начинаем с e = d, так как e строго больше каждого из слагаемых
                e = d
                while e ** 5 < total:
                    e += 1
                
                # Если нашли точное совпадение
                if e ** 5 == total:
                    print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
                    print(f"Сумма a + b + c + d + e = {a + b + c + d + e}")
                    found = True
                    break