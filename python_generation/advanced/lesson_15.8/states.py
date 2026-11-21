sorted_data = sorted(data, reverse=True, key=lambda state: state[1][-1])

for pop, name in sorted_data:
    print(f'{name}: {pop}')