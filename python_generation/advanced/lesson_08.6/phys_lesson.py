s1 = {int(x) for x in input().split()}
s2 = {int(x) for x in input().split()}
s3 = {int(x) for x in input().split()}

result = s3 - s1 - s2
print(*sorted(result, reverse=True))