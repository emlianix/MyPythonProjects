def get_last_index(data, value):
    if value not in data:
    	return 'ERROR!'
    else:
    	for i in range(len(data) -1, -1, -1):
    		if data[i] == value:
    			return i

data = eval(input())
value = eval(input())

print(get_last_index(data, value))