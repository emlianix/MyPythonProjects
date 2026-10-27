s1 = {int(x) for x in input().split()}
s2 = {int(x) for x in input().split()}
s3 = {int(x) for x in input().split()}

result = (s1 & s2) - s3

print(*sorted(result, reverse=True))