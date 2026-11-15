def digits_sum(number):
    return sum(int(x) for x in str(number))

def sort_key(n):
    return (digits_sum(n), n)


nums = [int(x) for x in input().split()]
print(*sorted(nums, key=sort_key))