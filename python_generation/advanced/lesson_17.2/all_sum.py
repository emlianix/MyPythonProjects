from functools import reduce
from operator import add

file = open(input())
num_list = list(map(int, file.readlines()))
file.close()
print(reduce(add, num_list))