from math import floor

# 🔶 Меню программы
def start_app():
	print()
	print(' /\\_/\\  \n( o.o )\n > ^ < ')
	print()
		
		
# 🔶 Расчёт комиссии одного чека
def get_comm_for_receipt(receipt):
	if receipt < 80:
		return 0
	elif receipt < 100:
		return 1
	elif receipt < 140:
		return 2
	elif receipt < 220:
		return 3
	elif receipt < 240:
		return 4
	elif receipt < 320:
		return 5
	elif receipt < 340:
		return 6
	elif receipt < 380:
		return 7
	elif receipt < 460:
		return 8
	elif receipt < 600:
		return 9
	else:
		return 15  # на случай, если отдельный чек >= 600
		
		
# 🔶 Комиссия с иностранцев: 3% от суммы, округлённое
def calc_foreign_comm(total):
	foreign_comm = total * 0.03
	return floor(foreign_comm + 0.5)
	
	
start_app()

receipts = [int(x) for x in input("🔅 Введите суммы чеков через пробел: ").split()]
total_sum = sum(receipts)
total_comm = 0

if total_sum < 600:  # считаем комиссию отдельно для каждого чека
	
	print()
	for i in range(len(receipts)):
		comm = get_comm_for_receipt(receipts[i])
		total_comm += comm
		print(f"🔹 Чек {i + 1}: {receipts[i]} → комиссия ${comm}")
		
else:  # считаем по общему правилу >= 600
	total_comm = 15
	extra = total_sum - 600
	
	if extra > 0:
		add_blocks = extra // 140  # количество блоков по 140
		total_comm += add_blocks * 3

print()
print(f"💲 Общая сумма: ${total_sum}")
if total_sum >= 600:
	print(f"💲 Общая комиссия: $15 + $3 x {add_blocks} → ${total_comm}")
else:
	print(f"💲 Общая комиссия: ${total_comm}")
	
print()
foreign = input("🔅 Есть комиссия для иностранцев? y/n ")
if foreign == "y":
	print()
	receipts_f = [int(x) for x in input("🔅 Введите суммы чеков через пробел: ").split()]
	total_sum_f = sum(receipts_f)
	total_comm_f = calc_foreign_comm(total_sum_f)
	print()
	print(f"💲 Общая сумма: ${total_sum_f}")
	print(f"💲 Комиссия (3% от суммы): ${total_comm_f}")

if total_comm > 0 and foreign == "y":
    print()
    print(f"💲 Всего: ${total_comm + total_comm_f}")

print()
print(" 💰" * 3)