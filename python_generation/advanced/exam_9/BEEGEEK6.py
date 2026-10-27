m = int(input())
result = None

for _ in range(m):
    n = int(input())
    lesson = {input() for _ in range(n)}
    if result is None:
        result = lesson
    else:
        result &= lesson

for surname in sorted(result):
    print(surname)