def find_all(target, symbol):
    indexes = []
    for i in range(len(target)):
    	if target[i] == symbol:
    		indexes.append(i)
    return indexes

s = input()
char = input()

print(find_all(s, char))