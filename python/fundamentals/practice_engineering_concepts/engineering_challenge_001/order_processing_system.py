line = "=" * 36

print(line)
print('Project Phoenix')
print('Order Processing System')
print(line)

customer_name = input('Enter customer name: ').upper()
product_id = input('Enter product id: ').upper()
quantity_needed = int(input('Enter quantity: '))
customer_type = input('Enter customer type (REGULAR/PREMIUM): ').upper()

products = [
    {"id": "P101", "name": "Laptop", "category": "ELECTRONICS", "price": 55000, "stock": 5},
    {"id": "P102", "name": "Keyboard", "category": "ELECTRONICS", "price": 1500, "stock": 12},
    {"id": "P103", "name": "Chair", "category": "FURNITURE", "price": 7000, "stock": 4},
    {"id": "P104", "name": "Desk", "category": "FURNITURE", "price": 12000, "stock": 3},
    {"id": "P105", "name": "Monitor", "category": "ELECTRONICS", "price": 18000, "stock": 7}
]

base_discount = [{"min" : 0, "max" : 5000, "discount" : 0, "min_inclusive" : True, "max_inclusive" : False },
                 {"min" : 5000, "max" : 20000, "discount" : 5, "min_inclusive" : True, "max_inclusive" : False },
                 {"min" : 20000, "max" : 50000, "discount" : 10, "min_inclusive" : True, "max_inclusive" : False },
                 {"min" : 50000, "max" : float('inf'), "discount" : 15, "min_inclusive" : True, "max_inclusive" : True }]


customer_types = [{"type" : "REGULAR" , "discount" : 0},
                   {"type" : "PREMIUM" , "discount" : 5}]

product_found = False 

original_order_amount = 0
lower_end = False
upper_end = False
base_disc_ord_amount = 0
cust_disc_ord_amount = 0
total_discount = 0
discount_amount = 0
net_amount = 0
remaining_stock = 0

if quantity_needed <= 0 :
    print(f"The quantity ({quantity_needed}) which you entered is incorrect.")
elif customer_type != 'REGULAR' and customer_type != 'PREMIUM':
    print(f"Incorrect customer type you entered i.e. {customer_type}")

else:
    print(f'Customer name: {customer_name}')
    print(f'Customer type: {customer_type}')
    for p in products:
        if p['id'] == product_id:
            product_found = True
            if p['stock'] == 0:
                print("Out of stock")
            elif quantity_needed > p['stock']:
                print(f"Insufficient stock. Available is {p['stock']} and you need {quantity_needed}")
            else:
                print(f"Product name : {p['name']}")
                print(f"Unit price : {p['price']}")
                print(f"Quantity Needed : {quantity_needed}")
                original_order_amount = p['price'] * quantity_needed
                print(f"Original order amount : {original_order_amount}")

                for x in base_discount:
                    if x["min_inclusive"] == True:
                        lower_end = original_order_amount >= x["min"]
                    else:
                        lower_end = original_order_amount > x["min"]

                    if x["max_inclusive"] == True:
                        upper_end = original_order_amount <= x["max"]
                    else:
                        upper_end = original_order_amount < x["max"]

                    if lower_end and upper_end:
                        base_disc_ord_amount = x['discount']
                        break 

                print(f'Base discount % : {base_disc_ord_amount}')

                for y in customer_types:
                    if customer_type == y['type']:
                        cust_disc_ord_amount = y['discount']
                        break

                print(f'Customer discount % : {cust_disc_ord_amount}')

                total_discount = base_disc_ord_amount + cust_disc_ord_amount
                print(f'Total discount % : {total_discount}')

                discount_amount =  ( original_order_amount * total_discount / 100 ) 
                print(f'Discount amount : {discount_amount}')
                net_amount = original_order_amount - discount_amount
                print(f'Final Payable amount : {net_amount}')

                print(f'Payment succesful hence we can adjust the stock from inventory!')
                remaining_stock = p['stock'] - quantity_needed
                print(f'Stock remaining : {remaining_stock}')
                print(f'Updating the new stock list in inventory')
                p['stock'] = remaining_stock
            break

    if product_found == False :
        print(f'Product id you entered {product_id} is incorrect')






                

                

                    

            
            
