text = input()
start_index = text.find('[u-')

# Пока в строке есть зашифрованные символы
while start_index != -1:
    end_index = text.find(']', start_index)
    # Вырезаем номер символа между '[u-' и ']'
    code_str = text[start_index + 3:end_index]
    # Переводим номер в число и получаем символ Юникода
    char = chr(int(code_str))
    # Склеиваем строку: текст до '[u-', расшифрованный символ и текст после ']'
    text = text[:start_index] + char + text[end_index + 1:]
    # Ищем следующее вхождение '[u-'
    start_index = text.find('[u-')

print(text)