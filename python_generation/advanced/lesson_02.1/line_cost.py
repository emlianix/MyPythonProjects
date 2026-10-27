line = input()

cost_kop = len(line) * 60
rub = cost_kop // 100
kop = cost_kop % 100

print(f"{rub} р. {kop} коп.")