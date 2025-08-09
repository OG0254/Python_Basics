# Write a Python program that does the following:

# Create variables to store your:

# Full name (string)
# Age (integer)
# Country (string)
# Favorite number (integer or float)
# Is a programmer (boolean)
# Print all the information nicely with labels.

# Calculate how old you will be after 5 years and print the result.

# Multiply your favorite number by 10 and print the result.

# my code

# Name = str(input('Full name :'))
# Age = int(input('Enter age :'))
# Country = str(input('Enter country :'))
# Favouritenumber = float(input('Enter favourite number :'))
# IsaProgrammer = ('Is a programmer = True')

# print(f'{Name}\n')
# print(f'{Age}\n')
# print(f'{Country}\n')
# print(f'{Favouritenumber}\n')
# print(f'Is a programmer = True\n ')

# Mathage = int(input('Enter age'))
# print(f'addition', {Age + 5})
# Favouritenumber = float(input('Enter favourite number'))
# print(f'multiplication', {Favouritenumber * 10})

# cleaner code

# Getting user input
# Name = str(input('Full name: '))
# Age = int(input('Enter age: '))
# Country = str(input('Enter country: '))
# Favouritenumber = float(input('Enter favourite number: '))
# IsaProgrammer = True  # You can just assign the value directly

# Displaying the information
# print("\n--- Personal Info ---")
# print(f'Full Name: {Name}')
# print(f'Age: {Age}')
# print(f'Country: {Country}')
# print(f'Favourite Number: {Favouritenumber}')
# print(f'Is a Programmer: {IsaProgrammer}')

# Age after 5 years
# print(f'\nIn 5 years, you will be {Age + 5} years old.')

# Favourite number multiplied by 10
# print(f'Your favourite number times 10 is {Favouritenumber * 10}')

# Another example

# Write a Python program that:

# Asks the user to enter:

# Product name (string)
# Quantity (integer)
# Price per item (float)
# Calculates the total cost (Quantity × Price per item).

# Prints a short receipt:

# Product name
# Quantity
# Price per item
# Total cost

# Code
# productname = input('Product: ')
# quantity = int(input('Quantity: '))
# price = float(input('Price per item: '))

# total_cost = quantity * price  # you can also declare it here 1a

# print('\n--- Receipt---')
# print(f'Product: ', productname)
# print(f'Quantity: ', quantity)
# print(f'Price per item: ', price)
# print(f'Total cost: ', quantity * price)

# print(f'Total cost: total_cost) 1b


# Bonus Task Code: Two Items + Grand Total

# productname1 = input('Product1: ')
# quantity1 = int(input('Quantity: '))
# price1 = float(input('Price per item: '))
# total1 = quantity1 * price1

# more_items = input('Do you want to buy more items? (yes/no):')

# if  more_items == 'yes':
#    productname2 = input('Product2: ')
#    quantity2 = int(input('Quantity: '))
#    price2 = float(input('Price per item: '))
#    total2 = quantity2 * price2

#    more_items = input('Do you want to buy more items? (yes/no):')

#    if more_items == 'yes':
#        productname3 = input('Product3: ')
#        quantity3 = int(input('Quantity: '))
#        price3 = float(input('Price per item: '))
#        total3 = quantity3 * price3

#        grand_total = total1 + total2 + total3

#        print('\n---- Receipt----')
# print(f'Product1', quantity1 * price1) # example
#        print(f'{productname1}: {quantity1} * Kes {price1} = Kes {total1}')  # same code
# print(f'Product2', quantity2 * price2) #example
#        print(f'{productname2}: {quantity2} * Kes {price2} = Kes {total2}')  # same code
# print(f'Product3', quantity3 * price3) #example
#        print(f'{productname3}: {quantity3} * Kes {price3} = Kes {total3}')  # same code
#        print(f'Grand total: Kes {grand_total}')  # same code

#    else:
#        grand_total = total1 + total2

#        print('\n--- Receipt---')
#        print(f'{productname1}: {quantity1} * Kes {price1} = Kes {total1}')
#        print(f'{productname2}: {quantity2} * Kes {price2} = Kes {total2}')
#        print(f'Grand total: Kes {grand_total}')

# else:
#    print('\n---- Receipt ----')
#    print(f'{productname1}: {quantity1} * Kes {price1} = Kes {total1}')
#    print(f'Grand total: Kes {total1}')


# Bonus Task Code: Alot of Items + Grand Total  Example 2

products = []
grand_total = 0

while True:
    name = input("Product name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per item: "))
    total = quantity * price
    grand_total += total

    products.append({
        'name': name,
        'quantity': quantity,
        'price': price,
        'total': total
    })

    more = input("Do you want to buy more items? (yes/no): ")
    if more.lower() != 'yes':
        break

# Print the receipt
print("\n---- Receipt ----")
for product in products:
    print(
        f"{product['name']}: {product['quantity']} * Kes {product['price']} = Kes {product['total']}")
print(f"Grand total: Kes {grand_total}")
