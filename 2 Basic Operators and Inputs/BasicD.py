print('\n--- Discount Calculator ---')
price = float(input('Enter original price: '))
discount = float(input('Enter discount price: '))
discount_amount = (discount/100) * price
final_price = price - discount_amount

print('\n--- Receipt ---')
print(f'Original Price: {price}')
print(f'Discount Amount: {discount_amount}')
print(f'Final Price: {final_price}')
