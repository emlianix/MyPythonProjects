n = int(input())
sales = {}

for _ in range(n):
    buyer, item, count = input().split()
    if buyer not in sales:
        sales[buyer] = {}
    sales[buyer][item] = sales[buyer].get(item, 0) + int(count)

for buyer in sorted(sales):
    print(f"{buyer}:")
    for item in sorted(sales[buyer]):
        print(item, sales[buyer][item])