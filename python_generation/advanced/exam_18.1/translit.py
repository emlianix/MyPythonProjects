def transliterate(filename):
    table = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e',
        'ё': 'jo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'j', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
        'ч': 'ch', 'ш': 'sh', 'щ': 'shh', 'ъ': '*', 'ы': 'y', 'ь': "'",
        'э': 'je', 'ю': 'ju', 'я': 'ya'
    }

    with open(filename, encoding='utf-8') as f:
        text = f.read()

    result = []
    for ch in text:
        low = ch.lower()
        if low in table:
            tr = table[low]
            result.append(tr.capitalize() if ch != low else tr)
        else:
            result.append(ch)

    with open('transliteration.txt', 'w', encoding='utf-8') as f:
        f.write(''.join(result))