keys = {
    '1': '.,?!:',
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
    '0': ' '
}

# symbol -> required key presses
presses = {}
for digit in keys:
    chars = keys[digit]
    count = 1
    for ch in chars:
        presses[ch] = digit * count
        count += 1

message = input().lower()

result = ''
for ch in message:
    if ch in presses:
        result += presses[ch]

print(result)