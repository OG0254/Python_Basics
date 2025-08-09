print('--- Fruit Basket ---\n')
fruit = str(input('Enter name of fruit: ')).lower()

if fruit == 'apple' or fruit == 'banana' or fruit == 'mango':
    print(f'You selected a {fruit}')

else:
    print("We don't have that fruit. Try apple, banana, or mango")
