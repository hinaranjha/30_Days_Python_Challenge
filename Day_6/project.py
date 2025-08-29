# Project: "Basic Banking Functions"


# Create account
def create_account(name, initial_balance):
    return {'name': name, 'balance': initial_balance}


# deposit
def deposit(account, amount):
    account['balance'] += amount
    return account


# withdrawal 
def withdrawal(account, amount):
    if amount > account['balance']:
        return 'Insufficient Balance'
    account['balance'] -= amount
    return f"Balacnce after withdrawal {amount}: {account}"


# check balance
def check_balance(account):
    return f"Hi {account['name']}, Your current balance is {account['balance']}"

# declare the account variable 
account = create_account('name', 5000)

# call the function
print(deposit(account, 7000))
print(withdrawal(account, 2000))
print(check_balance(account))