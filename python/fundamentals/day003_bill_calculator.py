line = "=" * 36

print(line)
print('Project Phoenix')
print('Bill Calculator')
print(line)

item_name = input('Enter item name: ')
item_price = float(input('Enter item price: '))
qty = int(input('Enter quantity: '))
gst = float(input('Enter GST: '))

subtotal = item_price * qty 
gst_amt = subtotal * (gst / 100)
final_amt = subtotal + gst_amt

print(line)
print('Bill Summary')
print(line)

print(f'Item : {item_name}')
print(f'Price : {item_price}')
print(f'Quantity : {qty}')
print(f'Subtotal : {subtotal}')
print(f'GST : {gst} %')
print(f'Final Amount : {final_amt}')