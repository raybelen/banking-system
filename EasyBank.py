import random
stored_account = {}

def Create_Account():
    print('\n-----Welcome to Create Account Section-----')
    name = input('Enter your name: ')
    balance = float(input('Enter initial deposit: '))
    account_number = random.randint(1000 , 9999)
    stored_account[account_number] = {'Name': name, 'balance': balance}
    print(f'Hi {name}, Successfully created an account, Your account number is {account_number}!\nWelcome to BDO!\nYour balance is ₱{balance}')
    transac_again = input("Do you want to do another transaction? (yes/no): ").lower()
    if transac_again == 'yes':
        Transaction_Menu()
    else:
        Exit()

def Deposit_Funds():
    print('\n-----Welcome to Deposit Section-----')
    account_number = int(input('Enter account number: '))
    if account_number in stored_account:
        fund_deposit = float(input('Enter the amount to deposit: '))
        stored_account[account_number]['balance'] += fund_deposit
        print(f'Successfully deposited ₱{fund_deposit}. New Balance: ₱{stored_account[account_number]['balance']}')
    else:
        print('Invalid Account Number!')
    transac_again = input("Do you want to do another transaction? (yes/no): ").lower()
    if transac_again == 'yes':
        Transaction_Menu()
    else:
        Exit()
        
def Withdraw_Funds():
    print('\n-----Welcome to Withdraw Section-----')
    account_number = int(input('Enter account number: '))
    if account_number in stored_account:
        fund_withdraw = float(input('Enter the amount to withdraw: '))
        if fund_withdraw < stored_account[account_number]['balance']:
            stored_account[account_number]['balance'] -= fund_withdraw
            print(f'Successfully withdrew ₱{fund_withdraw}. New Balance: ₱{stored_account[account_number]['balance']}')
        else:
            print('Insuffient account balance!')
    else:
        print('Invalid Account Number!')
    transac_again = input("Do you want to do another transaction? (yes/no): ").lower()
    if transac_again == 'yes':
        Transaction_Menu()
    else:
        Exit()

def Check_Balance():
    print('\n-----Welcome to Check Balance Section-----')
    account_number = int(input('Enter account number: '))
    if account_number in stored_account:
        print(f'Your Balance is ₱{stored_account[account_number]['balance']}')
    else:
        print('Invalid Account Number!')
    transac_again = input("Do you want to do another transaction? (yes/no): ").lower()
    if transac_again == 'yes':
        Transaction_Menu()
    else:
        Exit()

def Exit():
    print('Thank you, have a nice day!')

def Transaction_Menu():
    print('\n-----Welcome to EasyBank-----')
    print('1 - Create Account')
    print('2 - Deposit')
    print('3 - WIthdraw')
    print('4 - Check Balance')
    print('5 - Exit')

    selection = int(input('Enter the number (1 - 5): '))
    match selection:
        case 1: Create_Account()
        case 2: Deposit_Funds()
        case 3: Withdraw_Funds()
        case 4: Check_Balance()
        case 5: Exit()
        case _: 
            try_again = input("Invalid selection, Try Again? (yes/no): ").lower()
            if try_again == 'yes':
                Transaction_Menu()
            else:
                Exit()

Transaction_Menu()