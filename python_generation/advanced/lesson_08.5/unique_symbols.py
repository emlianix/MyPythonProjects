n = int(input())
for _ in range(n):
    word = input().strip().lower()
    print(len(set(word)))