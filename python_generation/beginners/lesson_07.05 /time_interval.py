h1, m1, h2, m2 = int(input()), int(input()), int(input()), int(input())

current = h1 * 60 + m1
end = h2 * 60 + m2

while current <= end:
    h = current // 60
    m = current % 60
    
    # Добавляем '0' вручную, если число меньше 10
    if h < 10:
        h_str = "0" + str(h)
    else:
        h_str = str(h)
        
    if m < 10:
        m_str = "0" + str(m)
    else:
        m_str = str(m)
        
    print(f"{h_str}:{m_str}")
    current += 1