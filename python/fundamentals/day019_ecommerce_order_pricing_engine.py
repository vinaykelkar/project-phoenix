line = "=" * 36

print(line)
print('Project Phoenix')
print('E-commerce Order Pricing Engine')
print(line)

products = {
    "P101": {"name": "Laptop", "price": 55000},
    "P102": {"name": "Keyboard", "price": 1500},
    "P103": {"name": "Monitor", "price": 18000},
    "P104": {"name": "Chair", "price": 7000}
}

product_id = input('Enter product id : ').upper()
quantity = int(input('Enter Quantity : '))
cust_type = input('Enter customer type (REGULAR/PREMIUM) : ').upper()

customer_types = {'PREMIUM' : {"Discount" : 5},
                  'REGULAR' : {"Discount" : 0}}

def validate_inputs(prod_id,qty,c_type):
    if prod_id not in products:
        return False, f"Product id is incorrect"
    elif qty <= 0:
        return False, f"Quantity entered is incorrect"
    elif c_type not in customer_types:
        return False, f"Customer type is incorrect"
    return True, "Validation successful"

def calculate_subtotal(price,qty):
    subtotal = price * qty 
    return subtotal

def calculate_base_discount(gross_amt):
    if 0 <= gross_amt < 10000:
        return 0
    elif 10000 <= gross_amt < 50000:
        return 5
    else:
        return 10

def calculate_customer_discount(c_type):
    cust_discount = customer_types[c_type]["Discount"]
    return cust_discount

def calculate_discount_amount(gross_amt, t_discount):
    discount_amount = ( gross_amt * t_discount ) /100
    return discount_amount

def calculate_final_amount(gross_amt,disc_amt):
    net_amount = gross_amt - disc_amt
    return net_amount

is_valid, message = validate_inputs(product_id,quantity,cust_type)
if is_valid:
    print(f'{message}, Please proceed with transaction')
    product_name = products[product_id]["name"]
    print(f'Product : {product_name}')
    unit_price = products[product_id]["price"]
    print(f'Unit Price : {unit_price}')
    print(f'Quantity : {quantity}')
    print(f'')
    subtotal = calculate_subtotal(unit_price,quantity)
    print(f'Subtotal : {subtotal}')
    base_discount = calculate_base_discount(subtotal)
    print(f'Base Discount : {base_discount}%')
    customer_discount = calculate_customer_discount(cust_type)
    print(f'Customer Discount: {customer_discount}%')
    total_discount = base_discount + customer_discount
    print(f'Total Discount: {total_discount}%')
    discount_amount = calculate_discount_amount(subtotal,total_discount)
    print(f'Discount Amount: {discount_amount}')
    final_amount = calculate_final_amount(subtotal,discount_amount)
    print(f'Final amount: {final_amount}')
else:
    print(f"Error: Invalid inputs provided. Transaction cancelled. {message}")

