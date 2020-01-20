from bank_app_modules import (
    start_app,
    create_account,
    login,
    transaction,
    check_balance,
    accounts,
    new_transaction,
    deposit,
    withdraw,
    transfer
)

account_transaction_code = start_app()

account_user = None

if account_transaction_code == 1:
    users = create_account()
    accounts = users['accounts']
    account_user = users['new_account']
    print('\nAll accounts\n' + str(accounts))
    account_transaction_code = start_app()


def transaction_actions(account_user):
    while account_user == None:
        account_user = login()
        if account_user == None:
            users = create_account()
            accounts = users['accounts']
            account_user = users['new_account']
            print('\nAll accounts\n' + str(accounts))
    print(account_user)
    transaction_code = transaction()

    if transaction_code == 1:
        account_balance = check_balance(account_user)
        print('\nYour account balance is: ' + '=N=' + str(account_balance))
        ok = input('Press ENTER: ')
        while ok != '':
            ok = input('Press ENTER: ')
        return new_transaction()

    if transaction_code == 2:
        bank_deposit = deposit(account_user)
        amount_deposit = bank_deposit['amount']
        account_balance = bank_deposit['new_balance']
        print(
            '\nCredit: ' + '=N=' + str(amount_deposit) +
            '\nYour account balance is: ' + '=N=' + str(account_balance)
        )
        ok = input('Press ENTER: ')
        while ok != '':
            ok = input('Press ENTER: ')
        return new_transaction()

    if transaction_code == 3:
        bank_withdrawal = withdraw(account_user)
        withdrawal = bank_withdrawal['amount']
        account_balance = bank_withdrawal['new_balance']
        print(
            '\nDebit: ' + '=N=' + str(withdrawal) +
            '\nYour account balance is: ' + '=N=' + str(account_balance)
        )
        ok = input('Press ENTER: ')
        while ok != '':
            ok = input('Press ENTER: ')
        return new_transaction()

    if transaction_code == 4:
        fund_transfer = transfer(account_user)
        if fund_transfer != None:
            amount = fund_transfer['amount']
            account_balance = fund_transfer['new_balance']
            recipient = fund_transfer['recipient_email']
            recipient_balance = fund_transfer['recipient_balance']
            print(
                '\nTransaction type: Transfer' +
                '\nRecipient: ' + recipient +
                '\nDebit: ' + '=N=' + str(amount) +
                '\nYour account balance is: ' + '=N=' + str(account_balance) +
                '\nRecipient balance: ' + '=N=' + str(recipient_balance)
            )
            ok = input('Press ENTER: ')
            while ok != '':
                ok = input('Press ENTER: ')
            return new_transaction()


def transaction_function(account_user):
    transaction_action = transaction_actions(account_user)

    if transaction_action == 0:
        return print(
            '\nThank you for banking with us!' +
            '\nFrom: Tobi Akanji'
        )

    if transaction_action == 1:
        transaction_function(account_user)


if account_transaction_code == 2:
    transaction_function(account_user)
