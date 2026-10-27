n = int(input())

for h in range(24):
    for m in range(60):
        if h ** n == m:
            # Добавляем ведущий ноль к часам, если h < 10
            if h < 10:
                h_str = '0' + str(h)
            else:
                h_str = str(h)
            
            # Добавляем ведущий ноль к минутам, если m < 10
            if m < 10:
                m_str = '0' + str(m)
            else:
                m_str = str(m)
            
            print(h_str + ':' + m_str)