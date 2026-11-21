small_num = filter(lambda x: x <= 47 or x % 2 == 0, numbers)
div_num = map(lambda x: x // 2 if x % 2 == 0 else x, small_num)
print(*div_num)/