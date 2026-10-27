n = int(input())
target = "anton"

infected = []

for i in range(1, n + 1):
    s = input()
    target_index = 0

    for char in s:
        if char == target[target_index]:
            target_index += 1
            if target_index == len(target):
                infected.append(i)
                break

if infected:
    print(*infected)