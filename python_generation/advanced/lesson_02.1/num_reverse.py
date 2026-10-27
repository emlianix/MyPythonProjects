n = input()
result = int(n[:-5] + n[-5:][::-1])
print(result)