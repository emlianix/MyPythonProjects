result = {}

for pet, first_name, last_name, age in pets:
    owner = (first_name, last_name, age)
    result.setdefault(owner, []).append(pet)

print(result)