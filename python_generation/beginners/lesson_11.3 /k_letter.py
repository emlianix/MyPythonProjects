text = []
for _ in range(int(input())):
	text.append(input())
	
k = int(input())
k_string = ''
for str in text:
	if len(str) >= k:
		k_string += str[k - 1]
		
print(k_string)