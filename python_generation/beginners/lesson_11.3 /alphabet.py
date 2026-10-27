alphabet = []

for i in range(ord('a'), ord('z') + 1):
	alphabet.append(chr(i))
	
for i in range(len(alphabet)):
	alphabet[i] *= i + 1
	
print(alphabet)