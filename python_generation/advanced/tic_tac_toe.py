from random import choice
import time
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_field(field):
    emojis = {0: '⬜', 1: '❌', 2: '⭕'}
    for row in field:
        print(''.join(emojis[cell] for cell in row))

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

def who_goes_first():
    return choice(['player', 'comp'])

def get_user_move():
    pass

def get_computer_move():
    pass

def check_result():
    pass


def main_game():
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

