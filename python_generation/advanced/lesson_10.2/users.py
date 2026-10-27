users = [
    {'phone': '120-3518', 'name': 'Mike', 'city': 'Moscow'},
    {'name': 'Nadya', 'phone': '813-1618', 'city': 'Paris'},
    {'name': 'Sasha', 'phone': '449-3141', 'email': ''},
    {'phone': '876-9655', 'name': 'Alexei', 'surname': 'Tolinkov'}
    ]

names = [user['name'] for user in users if user['phone'].endswith('8')]
print(*sorted(names))