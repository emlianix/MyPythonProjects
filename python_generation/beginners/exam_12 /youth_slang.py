text = input().split()
words = [word[1:] + word[0] + 'ки' for word in text]
print(*words)