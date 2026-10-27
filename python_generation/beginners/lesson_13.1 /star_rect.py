def draw_box():
    for i in range(14):
    	if i == 0 or i == 13:
    		star_sep = '*'
    	else:
    		star_sep = ' '
    	print('*', '*', sep=star_sep * 8)
    
draw_box()