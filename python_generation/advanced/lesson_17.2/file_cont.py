file = open(input())
text = list(map(str.strip, file.readlines()))
print(*text, sep='\n')

file.close()