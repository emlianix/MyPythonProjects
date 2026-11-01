def show_top_categories(spendings, num):
    totals = {}
    for category, amount in spendings:
        totals[category] = totals.get(category, 0) + amount

    top = sorted(totals, key=totals.get, reverse=True)[:num]

    for category in sorted(top):
        print(category)