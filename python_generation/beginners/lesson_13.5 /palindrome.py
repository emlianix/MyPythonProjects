def is_palindrome(text):
    chars = [ch.lower() for ch in text if ch.isalpha()]
    return chars == chars[::-1]
    

txt = input()

print(is_palindrome(txt))