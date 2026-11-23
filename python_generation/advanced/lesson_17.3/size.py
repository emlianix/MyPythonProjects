def calc_file_size(filename: str) -> int:
    with open(filename, encoding="utf-8") as file:
        content = file.read()
    return sum(2 if ch == "\n" else 1 for ch in content)


n = int(input().strip())
results = []

for _ in range(n):
    filename = input().strip()
    results.append((filename, calc_file_size(filename)))

results.sort(key=lambda item: (-item[1], item[0]))

for filename, size in results:
    print(f"{filename} {size}B")