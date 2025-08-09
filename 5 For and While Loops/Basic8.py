# Order Processing System
# You’re building a basic order processing system for a small food delivery business. The system should:

# Continuously ask the user to enter a food item and its price.

# Add the price to the running total.

# Stop asking for input if the user types "done".

# After exiting the loop, print:

# The number of items ordered

# The total cost

# A thank-you message

print('--- Order Processing System ---\n')

total = 0
list_item = 0
all_items = ''  # One string to hold everything

while True:
    food_item = input('Enter food item: ').lower()
    if food_item == 'done':
        break
    price = int(input('Enter price: '))
    list_item += 1
    total += price
    print(f'Total cost: {total}')  # Add each item to the string
    all_items += f'{list_item}. {food_item.title()}\n'

print(f'\n🧾 Receipt:')
print(f'Items ordered: ')
print(all_items)
print(f'Total number of items: {list_item}')
print(f'Total cost: Kes.{total}')
print('Thank you for shopping with Ogada mini supermarket ')
