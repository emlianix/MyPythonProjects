def sum_mn_mx(n):
    return min(n) + max(n)

print(sorted(numbers, key=sum_mn_mx))