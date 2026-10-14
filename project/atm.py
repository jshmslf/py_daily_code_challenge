# phase 0: just the structure of a simple atm

balance = 0

def withdraw_money():
    global balance
    money_input = float(input('How much you will withdraw? >> '))
    
    if money_input <= balance:
        balance -= money_input
        print(f'New balance: ${balance}')
    else:
        print('Insufficient Balance')
    

def deposit_money():
    global balance
    money_input = float(input('How much money you will deposit? >> '))
    
    balance += money_input
    
    print(f'New balance: ${balance}')

def show_balance():
    print(f'${balance}')

while True:
    print('1: Withdraw money')
    print('2: Deposit money')
    print('3: Show Balance')
    print('0: Log Out')
    selected = int(input('>>'))
    
    match selected:
        case 1:
            withdraw_money()
        case 2:
            deposit_money()
        case 3:
            show_balance()
        case 0:
            break

