def mean(t):
    return sum(t) / len(t)

print(min(numbers, key=mean))
print(max(numbers, key=mean))