s = 0
mx = -10**6 - 1  # строго меньше минимально возможного
has_negative = False

for i in range(10):
    x = int(input())
    if x < 0:
        s += x
        has_negative = True
        if x > mx:
            mx = x

if has_negative == False:
    print("NO")
else:
    print(s)
    print(mx)