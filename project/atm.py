# phase 0: just the structure of a simple atm ✔️
# phase 1: register
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "accounts.txt")

def register():
    print("--- Account Registration ---")
    while True:
        # register username
        reg_username = input('Your Username: ').strip()
        
        if len(reg_username) == 0:
            print("Username can't be blank. Please try again.\n")
            continue
        
        # register amount
        reg_amount = input('Your first deposit: ')
        
        try:
            reg_amount = float(reg_amount)
        except ValueError:
            print("Amount should be a number.\n")
            continue
        
        reg_password = input('Your password (min. 6  characters): ')
        
        if len(reg_password) < 6:
            print("Password too short! It must be at least 6 characters.\n")
            continue
        
        print("Registration successful!")
        break
        
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f"{reg_username}, {reg_amount:.2f}, {reg_password}")

def main_screen():
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

# ===============================

balance = 0
is_register = False

while True:
    print("Welcome to ATM Machine!")
    print("=========================")
    print("|| 1. Login")
    print("|| 2. Register")
    print("|| 0. Exit")
    selected_key = int(input('>> '))

    match selected_key:
        case 1:
            pass
        case 2:
            register()
        case 0:
            print("Thank you! Come Again!")
            break
        case _:
            print('WARNING: Pick only 0 to 3')