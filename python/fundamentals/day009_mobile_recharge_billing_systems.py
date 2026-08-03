line = "=" * 36

print(line)
print('Project Phoenix')
print('Mobile Recharge Billing System')
print(line)

customer_name = input('Enter your name: ')
recharge_amount = float(input('Enter your recharge amount: '))
customer_type = input('Enter type of billing (PREPAID/POSTPAID): ')
allowed_types = ['PREPAID','POSTPAID']

cashback_below_299 = 0
cashback_299_to_599 = 5
cashback_600_and_above = 10
cashback = 0
total_cashback = 0
cashback_amount = 0
final_recharge_amount = 0

if customer_type.upper() in allowed_types and recharge_amount > 0:
    print(f'Customer name: {customer_name}')
    print(f'Customer Type: {customer_type}')
    print(f'Recharge Amount: {recharge_amount}')

    if recharge_amount < 299:
        print(f'Cashback %: {cashback_below_299}')
        cashback = cashback_below_299
    elif 299 <= recharge_amount <= 599:
        print(f'Cashback %: {cashback_299_to_599}')
        cashback = cashback_299_to_599
    else:
        print(f'Cashback %: {cashback_600_and_above}')
        cashback = cashback_600_and_above

    if customer_type.upper() == 'PREPAID':
        loyalty_cashback = 0

    elif customer_type.upper() == 'POSTPAID': 
        loyalty_cashback = 2

    total_cashback = cashback + loyalty_cashback
    cashback_amount = ( recharge_amount * total_cashback ) / 100
    final_recharge_amount = recharge_amount - cashback_amount

    print(f'Loyalty cashback %: {loyalty_cashback}')
    print(f'Total cashback %: {total_cashback}')
    print(f'Total cashback: {cashback_amount}')
    print(f'Final recharge cost: {final_recharge_amount}')

else:
    print(f'Either customer type or recharge amount is incorrect')






    

        
        



