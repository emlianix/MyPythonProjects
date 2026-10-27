n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]

ab = n + m - x
bc = m + k - y
ac = n + k - z

only_a = n - ab - ac + t
only_b = m - ab - bc + t
only_c = k - bc - ac + t
one = only_a + only_b + only_c

two = (ab - t) + (bc - t) + (ac - t)

none = a - (one + two + t)

print(one)
print(two)
print(none)