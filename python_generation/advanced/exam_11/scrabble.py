points = {}

groups = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ",
}

for score, letters in groups.items():
    for letter in letters:
        points[letter] = score

word = input().strip()
print(sum(points[ch] for ch in word))