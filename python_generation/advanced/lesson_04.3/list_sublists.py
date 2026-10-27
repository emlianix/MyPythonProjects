lst = input().split()

result = [[]]

for i in range(len(lst)):
    for j in range(i + 1, len(lst) + 1):
        result.append(lst[i:j])

print(result)