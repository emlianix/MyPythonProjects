def caesar_cipher(text, direction, language, shift):
    if direction == 'd':
        shift = -shift

    if language == "ru":
        lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
        upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        power = 32
    elif lang == "en":
        lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
        upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        power = 26
    else:
    	print('Wrong language')
    	return

    result = ''
    for ch in text:
        if ch in lower_alphabet:
            index = lower_alphabet.find(ch)
            result += lower_alphabet[(index + shift) % power]
        elif ch in upper_alphabet:
            index = upper_alphabet.find(ch)
            result += upper_alphabet[(index + shift) % power]
        else:
            result += ch

    return result


print('=== Program: Caesar Cipher ===')
direct = input('Encrypt or decrypt? e/d ').strip().lower()
lang = input('Language (ru/en): ').strip().lower()
step = int(input('Shift: '))
txt = input('Text: ')

print(caesar_cipher(txt, direct, lang, step))