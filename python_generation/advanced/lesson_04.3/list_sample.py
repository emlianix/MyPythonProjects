n = int(input())
my_list = []

for _ in range(n):
    my_list.append(list(range(1, n +1)))
    
print(*my_list, sep="\n")