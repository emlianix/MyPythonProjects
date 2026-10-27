def print_fio(name, surname, patronymic):
	print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep='')
	
n, s, p = input(), input(), input()

print_fio(n, s, p)