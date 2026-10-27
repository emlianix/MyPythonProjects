def print_perm_time_call(msc_time):
    parts = msc_time.split(':')
    hours = int(parts[0]) + 2
    
    if hours < 10:
    	p_hours = '0' + str(hours)
    else:
    	p_hours = str(hours)
    
    print(f'Созвон будет в {p_hours}:{parts[1]}.')


time = input()

print_perm_time_call(time)