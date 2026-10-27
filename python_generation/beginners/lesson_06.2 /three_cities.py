city1, city2, city3 = input(), input(), input()

len1, len2, len3 = len(city1), len(city2), len(city3)

if len1 == min(len1, len2, len3):
    print(city1)
elif len2 == min(len1, len2, len3):
    print(city2)
else:
    print(city3)

if len1 == max(len1, len2, len3):
    print(city1)
elif len2 == max(len1, len2, len3):
    print(city2)
else:
    print(city3)