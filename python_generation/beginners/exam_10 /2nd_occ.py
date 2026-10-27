s = input()
cnt = s.count('f')

if cnt == 0:
    print(-2)
elif cnt == 1:
    print(-1)
else:
    first_idx = s.find('f')
    second_idx = s.find('f', first_idx + 1)
    print(second_idx)