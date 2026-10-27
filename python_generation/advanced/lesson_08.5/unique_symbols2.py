n = int(input())
chars = set()

for _ in range(n):
    word = input().strip().lower()
    for ch in word:
        chars.add(ch)
        
print(len(chars))