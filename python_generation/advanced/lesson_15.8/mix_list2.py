sorted_lst = sorted(mixed_list, key=lambda x: (isinstance(x, str), x))
print(*sorted_lst)