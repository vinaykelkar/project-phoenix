line = "=" * 36

print(line)
print('Project Phoenix')
print(line)

name = input('Enter your name: ')
balance = float(input('Account Balance: '))
withdrawal_amount = int(input('How much money you want to withdraw?: '))

print(f'Hello {name}')
print(f'This is your account balance {balance}')

if balance <= 0 or withdrawal_amount <= 0:
    print(f'Invalid account balance or withdrawal amount')
elif 0 < balance < 501:
    print(f'Can not make withdrawal if balance is less than or equal to 500 per rules')
else:
    if withdrawal_amount > balance:
        print(f'Insufficient balance')
    elif balance - withdrawal_amount > 499:
        print(f'Transaction Successful')
        print(f'Remaining Balance: {balance - withdrawal_amount}')
    else:
        print(f'EMinimum bvalance of 500 must be maintained')


