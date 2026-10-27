def print_case_counts(s):
    u_cnt = 0
    l_cnt = 0
    
    for ch in s:
    	if ch.isalpha():  # True == 1, False == 0
    		u_cnt += ch.isupper()
    		l_cnt += not ch.isupper()
    	else:
    		continue
	
    print(f'Букв в верхнем регистре: {u_cnt}')
    print(f'Букв в нижнем регистре: {l_cnt}')

text = input()

print_case_counts(text)