poet_data = ('Пушкин', 1799, 'Санкт-Петербург')

poet_list = list(poet_data)
poet_list[2] = 'Москва'
poet_data = tuple(poet_list)

print(poet_data)