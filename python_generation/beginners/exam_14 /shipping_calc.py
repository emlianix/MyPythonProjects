# объявление функции
def get_shipping_cost(quantity):
    total = 1000 + 120 * (quantity - 1)
    return total

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))