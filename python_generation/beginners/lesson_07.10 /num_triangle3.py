n = int(input())

for i in range(1, n + 1):
    # Печатаем возрастающую часть (от 1 до i)
    for j in range(1, i + 1):
        print(j, end="")
    
    # Печатаем убывающую часть (от i - 1 до 1)
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()