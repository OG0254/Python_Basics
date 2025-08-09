print('--- Simple Inventory Checker ---\n')

total = 0

items = int(input('How many items do want? '))

for x in range(1, items + 1):
    name = str(input(f'Item {x} name: ')).lower()
    quantity = int(input('Quantity: '))
    price = float(input('Price per unit: '))
    sub_total = quantity * price
    total += sub_total
    print(f'Total cost for {name} is {quantity * price}: ')

print(f'\nGrand total for all items is: {total}')
