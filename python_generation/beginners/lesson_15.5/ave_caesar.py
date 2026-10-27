text = input()
words = text.split(' ')

for word in words:
    # Длина сдвига — только количество английских букв в слове
    shift = sum(1 for char in word if char.isalpha())
    for char in word:
        if 'a' <= char <= 'z':
            print(chr((ord(char) - ord('a') + shift) % 26 + ord('a')), end='')
        elif 'A' <= char <= 'Z':
            print(chr((ord(char) - ord('A') + shift) % 26 + ord('A')), end='')
        else:
            print(char, end='')
    # Печатаем пробел после каждого слова (кроме последнего)
    if word != words[-1]:
        print(' ', end='')

print()  # Перенос строки в конце