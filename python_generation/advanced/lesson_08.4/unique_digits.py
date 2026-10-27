num = [int(x) for x in input().split)]
num_set = set(num)

if len(num) == len(num_set):
    print("YES")
else:
    print("NO")