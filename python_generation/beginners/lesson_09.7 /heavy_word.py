heavy_word = ""
max_uni = 0

for i in range(4):
	word = input()
	sum = 0
	for char in word:
		sum += ord(char)
	if sum > max_uni:
		max_uni = sum
		heavy_word = word
		
print(heavy_word)