parts = input().split('-')

# Получаем список длин только тех частей, которые состоят из цифр
digit_lens = [len(p) for p in parts if p.isdigit()]

# 7-abc-def-hijk (4 части, первая равна '7', остальные — цифры нужной длины)
if len(parts) == 4 and parts[0] == '7' and digit_lens[1:] == [3, 3, 4]:
    print('YES')
# abc-def-hijk (3 части, все — цифры нужной длины)
elif len(parts) == 3 and digit_lens == [3, 3, 4]:
    print('YES')

else:
    print('NO')