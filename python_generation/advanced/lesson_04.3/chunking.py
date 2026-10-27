def chunked(string, size):
    res = []
    for i in range(0, len(string), size):
        res.append(string[i:i + size])
    return res


s = input().split()
n = int(input())

print(chunked(s, n))