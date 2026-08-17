line = "=" * 36

print(line)
print('Project Phoenix')
print('Banking Transaction System')
print(line)

accounts = {
    "A101": {"name": "Amit", "balance": 50000},
    "A102": {"name": "Neha", "balance": 30000},
    "A103": {"name": "Rahul", "balance": 75000}
}

account_id = input('Please enter account id : ').upper()
tran_type = input('Enter transaction type (DEPOSIT/WITHDRAW) : ').upper()
amount = float(input('Please enter amount : '))
tran_types = ['DEPOSIT','WITHDRAW']

def validate(acct_id,trans_chosen,amt):
    if acct_id not in accounts:
        print(f'Please enter valid account id')
        return False
    elif trans_chosen not in tran_types:
        print(f'Please enter valid transaction type viz. DEPOSIT or WITHDRAW')
        return False
    elif amt <= 0:
        print(f'Please enter valid amount to either deposit or withdraw')
        return False
    return True

def deposit(acct_id,amt):
    previous_balance = accounts[acct_id]["balance"]
    print(f'Previous Balance is : {previous_balance}')
    print(f'Deposit Amount : {amt}')
    new_balance = previous_balance + amt
    print(f'New Balance : {new_balance}')
    accounts[acct_id]["balance"] = new_balance

def withdraw(acct_id,amt):
    previous_balance = accounts[acct_id]["balance"]
    print(f'Previous Balance is : {previous_balance}')
    print(f'Withdrawal Amount : {amt}')
    if amt > previous_balance:
        print(f'Insufficient balance')
        print(f'Available Balance is : {previous_balance}')
    else:
        new_balance = previous_balance - amt
        print(f'New Balance : {new_balance}')
        accounts[acct_id]["balance"] = new_balance

# Main Execution Flow Control
if validate(account_id, tran_type, amount):
    print(f'Account id : {account_id}')
    print(f'Transaction Type : {tran_type}')
    print(f'Amount : {amount}\n')

    if tran_type == 'DEPOSIT':
        deposit(account_id,amount)
    elif tran_type == "WITHDRAW":
        withdraw(account_id, amount)