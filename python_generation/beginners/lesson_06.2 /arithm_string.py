s1, s2, s3 = input(), input(), input()
l1, l2, l3 = len(s1), len(s2), len(s3)

# Средний элемент равен (сумма всех элементов - min - max)
mn = min(l1, l2, l3)
mx = max(l1, l2, l3)
mid = (l1 + l2 + l3) - mn - mx

if mid - mn == mx - mid:
    print("YES")
else:
    print("NO")