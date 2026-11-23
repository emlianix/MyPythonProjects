from random import choice


def ask_for_game(first_time=True):
    if first_time:
        greetings = [
            'Hello! Would you like to play?',
            'Good time of day! Want to play?',
            'Hello! How about the game?'
        ]
    else:
        greetings = [
            'Shall we play again?',
            'Want to play again?',
            'Do you want to do it again?'
        ]

    question = choice(greetings)  # picked once, so the same question repeats

    while True:
        answer = input(f'{question} y/n ').strip().lower()
        if answer == 'y':
            print('*')  # placeholder: the game starts here
            return
        elif answer == 'n':
            exit()
        else:
            print('Try again!')


# test
ask_for_game()
ask_for_game(False)