accounts = [
    {
        'email': 'john.doe@vgg.org',
        'password': 'qwerty123',
        'balance': 3000
    },
    {
        'email': 'jane.don@vgg.org',
        'password': 'uiop901',
        'balance': 10000
    },
    {
        'email': 'mike.moose@vgg.org',
        'password': 'asdf1999',
        'balance': 5000
    }
]


def start_app():
    print('\nVGG BANKING APPLICATION\nBy: Tobi Akanji\n')
    print('Press 1: create account\nPress 2: transaction')
    try:
        account_transaction_code = int(input('Input code: '))
        return account_transaction_code
    except ValueError:
        print('\nInvalid entry.\nFollow through with the instructions properly.')
        return start_app()


def create_account():
    print('\n\nSign up to create user account\n')
    email = input('Input email: ')
    for account in accounts:
        while account['email'] == email:
            print('Account already exists. Login to continue.')
            return create_account()
    password = input('input password: ')
    while len(password) < 6:
        print('Password not strong')
        return create_account()
    new_account = {
        'email': email,
        'password': password,
        'balance': 0
    }
    accounts.append(new_account)
    return {
        'accounts': accounts,
        'new_account': new_account
    }


def login():
    print('\nLogin to make your desired transaction')
    email = input('Input email: ')
    password = input('input password: ')
    for account in accounts:
        if (account['email'] == email and account['password'] == password):
            return account
    else:
        return print('\nInvalid email or password')


def transaction():
    print(
        '\nType in the code respective to the desired transaction\n' +
        'Press 1: check balance\n' +
        'Press 2: deposit\n' +
        'Press 3: withdraw\n' +
        'Press 4: transfer'
    )
    try:
        transaction_code = int(input('Input code: '))
        return transaction_code
    except ValueError:
        print('\nInvalid entry.')
        return transaction()


def check_balance(account):
    return account['balance']


def deposit(account):
    print('\nDeposit money into your account')
    try:
        amount = float(input('Amount: '))
        account['balance'] += amount
        return {'amount': amount, 'new_balance': account['balance']}
    except ValueError:
        print('\nInvalid entry.\nInput the money value.')
        return deposit(account)


def withdraw(account):
    print('\nWithdraw money from your account')
    try:
        amount = float(input('Amount: '))
        if amount < 0:
            print('No negatives error')
            return withdraw(account)
        if account['balance'] - amount < 0:
            print('Insufficient fund!')
            return {'amount': 0, 'new_balance': account['balance']}
        account['balance'] -= amount
        return {'amount': amount, 'new_balance': account['balance']}
    except ValueError:
        print('\nInvalid entry.\nInput the money value.')
        return withdraw(account)


def transfer(account):
    print('\nTransfer funds to another account')
    recipient = None
    recipient_email = input('Input user email of other account: ')
    if recipient_email == account['email']:
        print(
            '\nEnter recipient email, not your own email.' +
            '\nUse the DEPOSIT option if you want to transfer funds to your account '
        )
        return transfer(account)
    for recipient_account in accounts:
        if recipient_account['email'] == recipient_email:
            recipient = recipient_account
            break
    else:
        print('\nSuch user does not exist')
        return transfer(account)

    try:
        amount = float(input('\nInput amount: '))
        if amount < 0:
            print('No negatives error')
            return transfer(account)
        if account['balance'] - amount < 0:
            print('\nInsufficient fund')
            return transfer(account)
        account['balance'] -= amount
        recipient['balance'] += amount
        return {
            'amount': amount,
            'new_balance': account['balance'],
            'recipient_email': recipient_email,
            'recipient_balance': recipient['balance']
        }
    except ValueError:
        print('\nInvalid entry.\nInput the money value.')
        return transfer(account)


def new_transaction():
    try:
        transaction_response = int(input(
            '\nWill you like to perform another transaction?' +
            '\nPress 0: NO' +
            '\nPress 1: YES' +
            '\nInput response: '
        ))
        return transaction_response
    except ValueError:
        print('\nInvalid entry.')
        return new_transaction()
