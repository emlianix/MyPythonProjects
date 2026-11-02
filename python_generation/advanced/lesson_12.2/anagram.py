import random

def get_anagram(word):
    chars = list(word)
    anagram = random.shuffle(chars)
    return ().join(*anagram)

print(get_anagram(input()))