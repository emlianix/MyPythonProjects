import random


def get_word(words):
    word = random.choice(words)
    return word.upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


def play(word):
    word_completion = "_" * len(
        word
    )  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6

    print("Let's play a word-guessing game!")
    print(display_hangman(tries))
    print(word_completion)

    guess = input("Enter a word or letter: ")
    if not guess.isalpha():
        print("Error: enter a word or a letter!")
    elif guess in guessed_letters or guess in guessed_words:
        print("You've already tried this word/letter!")
    elif guess in word:
        word_completion = word_completion.replace("_", guess)
        guessed_letters.append(guess)
        guessed_words.append(guess)
        tries -= 1
        display_hangman(tries)
    elif guess == word:
        print("Congatulations, you guessed the word! You won!")
    elif guess not in word:
        guessed_letters.append(guess)
        guessed_words.append(guess)
        tries -= 1
        display_hangman(tries)
        print("Try again")


word_list = [
    "apple",
    "beach",
    "clock",
    "cloud",
    "dance",
    "earth",
    "flame",
    "glass",
    "house",
    "lemon",
    "music",
    "ocean",
    "bridge",
    "castle",
    "dragon",
    "forest",
    "garden",
    "island",
    "jungle",
    "knight",
    "planet",
    "rocket",
    "awkward",
    "blizzard",
    "crypt",
    "galaxy",
    "haiku",
    "ivory",
    "jinx",
    "matrix",
    "oxygen",
    "rhythm",
    "vortex",
]

play(get_word(word_list))