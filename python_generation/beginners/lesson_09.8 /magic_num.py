w1 = input()
w2 = input()
w3 = input()
w4 = input()

max_w = max(w1, w2, w3, w4)
min_w = min(w1, w2, w3, w4)
max_idx = ord(max_w[-1])
min_idx = ord(min_w[-1])
result = (max_idx * min_idx) ** 2

print(result)