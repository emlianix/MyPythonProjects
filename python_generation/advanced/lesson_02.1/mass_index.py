weight = float(input())
height = float(input())

idx = weight / height**2
if 18.5 <= idx <= 25:
	print("Оптимальная масса")
elif idx < 18.5:
	print("Недостаточная масса")
else:
	print("Избыточная масса")