lazy import random
lazy import os
lazy import time

player

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def pause():
    input('\nPress Enter to continue...')

def read_number():
    num = input('Enter an integer non-negative number: ')
    while not num.isdecimal():
        num = input('Wrong input! Try again. ')
    return int(num)

def show_player_info(player, show_time=True):
    print(f"Cash flow: {player['cash_flow']}")
    print(f"Cash: {player['cash']}")
    print(f"Total debt: {player['total_debt']}")
    print(f"Passive income: {player['passive_income']}")
    print(f"Purchased assets: {player['assets']}")
    print(f"Salary: {player['salary']}")
    print(f"Ordinary expenses: {player['ordinary_expenses']}")
    print(f"Loan payment: {player['loan_payment']}")
    print(f"Total income: {player['total_income']}")
    print(f"Total expenses: {player['total_consumption']}")
    if show_time:
        print(f"Month and event number: {player['current_month']} and {player['event_number']}")

def offer_loan(player, missing):
    pass

def add_loan(player, amount):
    pass
    # Функция должна увеличить значение по ключу 'loan' на число amount и пересчитать платёж по кредиту (по ключу 'loan_payment').

def pay_loan(player):
    pass
    # Функция должна спрашивать у пользователя, на какую сумму он хочет погасить кредит. После этого тело кредита (по ключу 'loan' в словаре player) уменьшается на указанную сумму, а выплата по кредиту пересчитывается.

def get_random_event(random_events):
    pass
    # выбирает и затем возвращает случайное событие из списка random_events с учетом веса события

def apply_random_event(player):
    get_random_event()
    # получает случайное событие через функцию get_random_event(), а затем применяет его: изменяет количество свободных средств, зарплату или расходы на проживание.

def month_recalculate(player):
    pass
    # подсчитывает общие расходы и доходы
    # вычисляет денежный поток
    # пополняет количество свободных денежных средств (по ключу 'cash' в словаре player)
    # делает выплату по кредиту
    # перерасчитывает процент по кредиту

def offer_investment(player):
    pass
    # предлагает игроку купить один из активов, выбрав его случайным образом. Если пользователь соглашается, происходит вызов функции buy_asset().

def buy_asset(player, asset):
    pass

def create_asset_name(player, asset):
    pass

def play_month():
    pass

player = {
    'cash_flow': ...,
    'cash': ...,
    'total_debt': ...,
    'passive_income': ...,
    'assets': [..., ..., ...],
    'salary': ...,
    'ordinary_expenses': ...,
    'loan_payment': ...,
    'total_income': ...,
    'total_consumption': ...,
    'current_month': ...,
    'event_number': ...,
}

random_events = []