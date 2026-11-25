from random import choice, randint
import time
import os

emojis = {0: '⬜', 1: '❌', 2: '⭕'}

def show_field(field):
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

def get_user_move(field):
    while True:
        parts = input('Your move (row col): ').split()
        if len(parts) != 2 or parts[0] not in ('1', '2', '3') or parts[1] not in ('1', '2', '3'):
            print('Wrong input! Enter two numbers from 1 to 3, separated by a space.')
            continue
        row = int(parts[0]) - 1
        col = int(parts[1]) - 1
        if field[row][col] != 0:
            print('That cell is taken.')
        else:
            return row, col

def get_computer_move(field):
    while True:
        move = (randint(0, 2), randint(0, 2))
        if field[move[0]][move[1]] == 0:
            return move

def check_result(field):
    lines = [
        [(0,0),(0,1),(0,2)], [(1,0),(1,1),(1,2)], [(2,0),(2,1),(2,2)],  # rows
        [(0,0),(1,0),(2,0)], [(0,1),(1,1),(2,1)], [(0,2),(1,2),(2,2)],  # columns
        [(0,0),(1,1),(2,2)], [(0,2),(1,1),(2,0)],  # diagonals
    ]
    for a, b, c in lines:
        if field[a[0]][a[1]] != 0 and field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]]:
            return field[a[0]][a[1]]  # 1 or 2 = the winner
    if all(cell != 0 for row in field for cell in row):
        return 'draw'
    return None  # game continues

def main_game():
    other = {'player': 'computer', 'computer': 'player'}
    first = True

    while True:
        answer = input(f'{ask_for_game(first)} y/n ').strip().lower()
        if answer == 'y':
            first = False
            turn = who_goes_first()
            marks = {turn: 1, other[turn]: 2}
            print(f'The {turn} goes first ❌')
            board = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ]

            while True:
                clear_console()
                show_field(board)
                if turn == 'player':
                    r, c = get_user_move(board)
                else:
                    print('Computer is thinking...')
                    time.sleep(1)
                    r, c = get_computer_move(board)
                    message = f'Computer plays: {r + 1} {c + 1}'
                board[r][c] = marks[turn]

                result = check_result(board)
                if result is not None:
                    clear_console()
                    show_field(board)
                    if message and turn == 'computer':
                        print(message)
                    print("It's a draw!" if result == 'draw' else f'The {turn} wins!')
                    break  # back to "play again?"
                turn = other[turn]

        elif answer == 'n':
            return
        else:
            print('Try again!')

main_game()