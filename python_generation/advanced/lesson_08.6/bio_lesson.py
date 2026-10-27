a = set(input().split())
b = set(input().split())
c = set(input().split())

all_marks = set()
for i in range(1, 11):
    all_marks.add(str(i))

missing = all_marks - (a | b | c)

result = sorted(int(x) for x in missing)
print(*result)