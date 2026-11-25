def decimal_any(num, base):
    if num == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # алфавит для систем счисления до 36-ричной
    result = ""
    integer_quot = num
    
    while integer_quot > 0:
        remainder = integer_quot % base  # остаток
        digit = digits[remainder]  # получаем нужный символ
        result = digit + result  # добавляем символ В НАЧАЛО строки
        integer_quot //= base  # обновляем частное
        
    return result


direction = input('Decimal to any (1) or any to decimal (2)? ')
system = int(input('Numeral system base: '))
n = int(input('Input number: '))

if direction == '1':
	print(decimal_any(n, system))
else:
	print(int(str(n), system))