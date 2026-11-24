from random import choice, randint
import time
import os

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
    return choice(greetings)
    
def who_goes_first():
    return choice(['player', 'computer'])

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_user_move():
    move = tuple(map(int, input().split()))
    return move

def get_computer_move():
    x = randint(0, 2)
    y = randint(0, 2)
    move = (x, y)

def check_result():
    pass


def main_game():
    first = True
    
    while True:
        answer = input(f'{ask_for_game(first)} y/n ').strip().lower()
        if answer == 'y':
            
            # The game starts here
            first = False
            print(f'The {who_goes_first()} goes first ❌')
            field = [
                [0, 0, 0], 
                [0, 0, 0], 
                [0, 0, 0]
            ]
            
        elif answer == 'n':
            exit()
        else:
            print('Try again!')