line = "=" * 36

print(line)
print('Project Phoenix')
print('Utility Billing System')
print(line)

customer_name = input('Enter customer name: ').upper()
customer_type = input('Enter category you belong to (RESIDENTIAL/COMMERCIAL): ').upper()
no_of_units = float(input('Enter units consumed: '))
category = ["RESIDENTIAL","COMMERCIAL"]

res_billing_slabs = [{"min" : 0, "max" : 100, "rate": 5},
                     {"min" : 100, "max" : 300, "rate": 7},
                     {"min" : 300, "max": float('inf'), "rate": 10}]

comm_billing_slabs = [{"min" : 0, "max" : 100, "rate": 8},
                     {"min" : 100, "max" : 300, "rate": 10},
                     {"min" : 300, "max": float('inf'), "rate": 12}]

utility_bill = 0
green_energy_discount = 5
discount_amount = 0
utility_bill_post_discount = 0
billing_slabs = []

if customer_type not in category or no_of_units <= 0:
    print(f'Either customer type you entered {customer_type} is wrong or unit consumption value you entered {no_of_units} is incorrect')

else:
    print(f'Customer name: {customer_name}')
    print(f'Customer Category: {customer_type}')
    print(f'Units consumed: {no_of_units}')

    if customer_type == "RESIDENTIAL":
        billing_slabs = res_billing_slabs
    else:
        billing_slabs = comm_billing_slabs

    for slab in billing_slabs:
        #print(f"Checking slab: {slab['min']} to {slab['max']} at rate {slab['rate']}")
        if slab['min'] < no_of_units <= slab['max']:
            print(f"Rate Per unit: {slab['rate']}") 
            utility_bill = no_of_units * slab['rate']
            print(f'Electricity bill: {utility_bill}')
            break


    if no_of_units < 150:
        print(f'Green energy discount% : {green_energy_discount}')
        discount_amount = ( utility_bill * green_energy_discount) / 100
        print(f'Discount amount: {discount_amount}')
        utility_bill_post_discount = utility_bill - discount_amount

    else:
        print(f'Green energy discount% : {0}')
        print(f'Discount amount: {0}')
        utility_bill_post_discount = utility_bill

    print(f'Final Payable amount: {utility_bill_post_discount}')



                


