text = input().lower().split()
total = text.count('a') + text.count('an') + text.count('the')
print(f'Общее количество артиклей: {total}')