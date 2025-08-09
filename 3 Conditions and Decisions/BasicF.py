print('\n--- Electricity Bill Calculator ---')
print('0–50 units → 3.5 per unit')
print('51–150 units → 5.0 per unit')
print('151–300 units → 6.5 per unit')
print('301+ units → 8.0 per unit \n')
name = input('Enter your name: ')
unit = float(input('Enter units used: '))
if unit >= 300:
    rate = 8.0
    total_bill = unit * 8.0
elif unit >= 151:
    rate = 6.5
    total_bill = unit * 6.5
elif unit >= 51:
    rate = 5.0
    total_bill = unit * 5.0
elif unit >= 0:
    rate = 3.5
    total_bill = unit * 3.5
else:
    print('Not applicable')

if total_bill > 0:
    print(f'Hello {name} the total bill is: {total_bill}')
    print(f'Rate applied is: {rate}')
