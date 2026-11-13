def print_products(*args):
    pr_list = [x for x in args if type(x) == str and x != '']
    if not pr_list: # if len(pr_list) == 0:
        print('Нет продуктов')
        return

    for i in range(len(pr_list)):
        print(f'{i + 1}) {pr_list[i]}')