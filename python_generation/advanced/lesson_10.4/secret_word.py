s = input()
n = int(input())

freq_to_letter = {}
for _ in range(n):
    letter, cnt = input().split(':')
    freq_to_letter[int(cnt)] = letter.strip()

cnt = {}
for ch in s:
    cnt[ch] = cnt.get(ch, 0) + 1

print(''.join(freq_to_letter[cnt[ch]] for ch in s))