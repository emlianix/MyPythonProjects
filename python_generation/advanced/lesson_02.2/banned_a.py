word = input() + ' запретил букву'

alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

for letter in alphabet:
    if letter in word:
        print(word, letter)

        new_word = ''
        for ch in word:
            if ch != letter:
                new_word += ch

        while '  ' in new_word:
            new_word = new_word.replace('  ', ' ')
        word = new_word.strip()