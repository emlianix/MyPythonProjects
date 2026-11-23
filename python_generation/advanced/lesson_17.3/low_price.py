def load_prices(filename):
    prices = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            product, price_str = line.rsplit(":", 1)
            prices[product.strip()] = float(price_str.strip())
    return prices


shops = [
    ("Десяточка", load_prices("desyatochka.txt")),
    ("Кубит", load_prices("kubit.txt")),
    ("Полоса", load_prices("polosa.txt")),
]

n = int(input().strip())
query_products = [input().strip() for _ in range(n)]

cheapest_by_shop = {name: [] for name, _ in shops}

for product in query_products:
    available_prices = [
        store_prices[product]
        for _, store_prices in shops
        if product in store_prices
    ]
    if not available_prices:
        continue

    min_price = min(available_prices)
    for name, store_prices in shops:
        if product in store_prices and store_prices[product] == min_price:
            cheapest_by_shop[name].append(product)

for name, _ in shops:
    print(f"{name}:")
    if cheapest_by_shop[name]:
        print(", ".join(cheapest_by_shop[name]))
    else:
        print("–")