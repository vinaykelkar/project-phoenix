
line = "=" * 36

print(line)
print('Project Phoenix')
print('Product Inventory Search System')
print(line)

product_details = [{"Product_id" : "P101", "Product" : "Laptop", "Category" : "Electronics", "Price":55000, "Stock": 5},
                   {"Product_id" : "P102", "Product" : "Keyboard", "Category" : "Electronics", "Price":1500, "Stock": 12},
                   {"Product_id" : "P103", "Product" : "Chair", "Category" : "Furniture", "Price":7000, "Stock": 0},
                   {"Product_id" : "P104", "Product" : "Desk", "Category" : "Furniture", "Price":12000, "Stock": 3},
                   {"Product_id" : "P105", "Product" : "Monitor", "Category" : "Electronics", "Price":18000, "Stock": 7}]

product_id= input('Enter product id: ').upper()
product_qty = int(input('Enter Quantity Required: '))
total_cost = 0
remaining_stock = 0
product_found = 0

if product_qty <= 0:
    print(f'{product_qty} you entered is invalid')
else:
    for x in product_details:
        if product_id != x['Product_id']:
            continue
        else:
            if x["Stock"] == 0:
                print(f" Sorry, {x['Product']} is out of stock")
                product_found = product_found + 1
                break
            elif product_qty > x["Stock"]:
                print(f"Insuffcient stock")
                print(f"Available stock / quantity for {x['Product']} is: {x["Stock"]}")
                product_found = product_found + 1
                break
            else:
                print(f"Product Id: {x['Product_id']}")
                print(f"Product : {x['Product']}")
                print(f"Category: {x['Category']}")
                print(f"Price : {x['Price']}")
                print(f"Quantity purchased: {product_qty}")
                total_cost = x['Price'] * product_qty
                print(f"Total cost: {total_cost}")
                remaining_stock = x['Stock'] - product_qty
                print(f"Remaining Stock: {remaining_stock}")
                product_found = product_found + 1
                break

    if product_found != 1:
        print(f'You entered invalid product id {product_id}')

        
