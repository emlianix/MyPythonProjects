from functools import reduce

big_cities = filter(lambda city: city[1] > 10000000 and city[2] == 'primary', data)
city_names = map(lambda city: city[0], big_cities)
one_string = reduce(lambda a, b: a + ', ' + b, sorted(city_names))

print(f'Cities: {one_string}')