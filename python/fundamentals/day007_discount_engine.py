line = "=" * 36

print(line)
print('Project Phoenix')
print('Discount Engine')
print(line)

name = input('Enter customer name: ')
shopping_amount = float(input('Enter shopping amount: '))
coupan_discount = 5
slab_1 = 0
slab_2 = 5
slab_3 = 10
slab_4 = 15

if shopping_amount <= 0 :
    print(f'Thank you for checking us out,do visit again!')
else:
    print(f'Thank you for shopping with us. Please find your bill details')
    print(f'Original Amount : {shopping_amount}')
    coupan_available = input('Do you have coupan? : ')
    if 1 <= shopping_amount <= 99 :
        print(f'Discount : {slab_1}%')
        shopping_amount_slab_1 = ( shopping_amount * slab_1 ) / 100
        shopping_amount = shopping_amount - shopping_amount_slab_1
        if coupan_available.upper() == 'YES':
            print(f'Coupan Discount : {coupan_discount}%')
            total_discount_amount = (shopping_amount * 5 ) / 100
        else:
            total_discount_amount = 0

        print(f'Total Discount amount : {total_discount_amount}')
        print(f'Final payable amount : {shopping_amount - total_discount_amount}')
    
    elif 100 <= shopping_amount <= 499.99:
        print(f'Discount : {slab_2}%')
        shopping_amount_slab_2 = ( shopping_amount * slab_2 ) / 100
        shopping_amount = shopping_amount - shopping_amount_slab_2
        if coupan_available.upper() == 'YES':
            print(f'Coupan Discount : {coupan_discount}%')
            total_discount_amount = (shopping_amount * 5 ) / 100
        else:
            total_discount_amount = 0

        print(f'Total Discount amount : {total_discount_amount}')
        print(f'Final payable amount : {shopping_amount - total_discount_amount}')

    elif 500 <= shopping_amount <= 999.99:
        print(f'Discount : {slab_3}%')
        shopping_amount_slab_3 = ( shopping_amount * slab_3 ) / 100
        shopping_amount = shopping_amount - shopping_amount_slab_3
        if coupan_available.upper() == 'YES':
            print(f'Coupan Discount : {coupan_discount}%')
            total_discount_amount = (shopping_amount * 5 ) / 100
        else:
            total_discount_amount = 0
            
        print(f'Total Discount amount : {total_discount_amount}')
        print(f'Final payable amount : {shopping_amount - total_discount_amount}')

    else:
        print(f'Discount : {slab_4}%')
        shopping_amount_slab_4 = ( shopping_amount * slab_4 ) / 100
        shopping_amount = shopping_amount - shopping_amount_slab_4
        if coupan_available.upper() == 'YES':
            print(f'Coupan Discount : {coupan_discount}%')
            total_discount_amount = (shopping_amount * 5 ) / 100
        else:
            total_discount_amount = 0
            
        print(f'Total Discount amount : {total_discount_amount}')
        print(f'Final payable amount : {shopping_amount - total_discount_amount}')





