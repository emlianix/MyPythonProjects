s = input().lower()
vow = "ауоыиэяюе"
cons = "бвгджзйклмнпрстфхцчшщ"
v_cnt = 0
c_cnt = 0

for c in s:
	if c in vow:
		v_cnt += 1
	if c in cons:
		c_cnt += 1
		
print(f"Количество гласных букв равно {v_cnt}")
print(f"Количество согласных букв равно {c_cnt}")