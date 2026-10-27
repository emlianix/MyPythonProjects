day = int(input())
weight = float(input())
target = 100 - day*0.2

if weight <= target:
	print("Все идет по плану")
else:
	print("Что-то пошло не так")
	
print(f"#{day} ДЕНЬ: ТЕКУЩИЙ ВЕС = {weight} кг, ЦЕЛЬ по ВЕСУ = {target} кг")