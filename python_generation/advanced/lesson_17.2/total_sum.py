file = open(input())
total = 0

for line in file:
    qty, price = map(int, line.strip().split('\t')[1:])
    total += qty * price
    
file.close()
print(total)