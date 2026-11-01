def bank(operation, id, amount, balances={}):
    if id not in balances:
        balances[id] = 0

    if operation == 'top up':
        balances[id] += amount
    elif operation == 'withdraw' or operation == 'pay':
        balances[id] -= amount
    elif operation == 'show balance':
        print(balances[id])