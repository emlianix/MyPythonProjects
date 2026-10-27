from statistics import mean

means = []
for i in range(len(numbers)):
    means.append(mean(numbers[i]))
print(means)