n = int(input())
synonyms = {}

for _ in range(n):
    a, b = input().split()
    synonyms[a] = b
    synonyms[b] = a

word = input()
print(synonyms[word])