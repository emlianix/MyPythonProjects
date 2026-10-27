n = int(input())
text = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = ''

for char in text:
    if char in alphabet:
        idx = alphabet.find(char)
        # Сдвигаем назад на n и используем % 26 для зацикливания алфавита
        new_idx = (idx - n) % 26
        result += alphabet[new_idx]

print(result)