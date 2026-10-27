def print_sorted_hyphen(s):
    s_list = s.split('-')
    s_list.sort()
    print(*s_list, sep='-')
    

text = input()

print_sorted_hyphen(text)