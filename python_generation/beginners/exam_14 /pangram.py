def is_pangram(text):
    text = text.lower()
    for i in range(ord("a"), ord("z") + 1):
        if chr(i) not in text:
            return False
    
    return True


text = input()

print(is_pangram(text))