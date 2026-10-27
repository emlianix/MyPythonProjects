def print_symbol_counts(word):
    word_lower = word.lower()
    ch_list = list(word_lower)
    ch_list.sort()
    last_printed = ""

    for ch in ch_list:
        if ch != last_printed:
            print(ch + ": " + str(ch_list.count(ch)))
            last_printed = ch  # запоминаем, что эта буква уже обработана


s = input()
print_symbol_counts(s)