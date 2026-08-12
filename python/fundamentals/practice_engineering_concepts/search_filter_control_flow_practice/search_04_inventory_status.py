line = "=" * 36

print(line)
print('Practice Engineering Concepts')
print('Search inventory status')
print(line)

inventory = [
    {"id": "P101", "name": "Laptop", "stock": 5},
    {"id": "P102", "name": "Keyboard", "stock": 0},
    {"id": "P103", "name": "Monitor", "stock": 8}
]

product_id = input('Pleae enter product id : ').upper()
condition_valid = False

for i in inventory:
    if i['id'] == product_id:
        condition_valid = True

        if i['stock'] == 0 :
            print(f'Product exists but stock is 0 i.e. {i['stock']}')
        elif i['stock'] > 0 :
            print(f'Product exists and stock is greater than 0 i.e. {i['stock']}')

if condition_valid == False:
    print(f'Product does not exist')
