print('--- Welcome to Fast Food Express ---\n')
item = str(input('What would you like to order? (burger/pizza): '))
# print(f'You ordered a {item} with {extra}.')

if item == 'burger' or item == 'pizza':
    extra = str(input('Do you want an extra? (drink/fries/none): '))
    if extra == 'drink' or extra == 'fries' or extra == 'none':
        print(f'You ordered a {item} with {extra}.')
    else:
        print('Check item placed')
else:
    print('nothing you have choosen is on the menu')
