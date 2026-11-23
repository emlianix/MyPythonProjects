file = open(input())
num_list = list(map(int, file.readlines()))
print(sum(num_list))