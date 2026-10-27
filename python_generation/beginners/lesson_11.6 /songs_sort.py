songs = []
for _ in range(int(input())):
	songs.append(input())
	
songs.sort()
print(*songs, sep='\n')