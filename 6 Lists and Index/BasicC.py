print('--- Smart Grocery Updater 🛒 ---\n')

grocery_list = ['Rice', 'Sugar', 'Salt', 'Tea', 'Coffee']

print(f'Current list: {grocery_list}')

# Ask user for an item to remove
remove_item = input('Which item would you like to remove? ').title()

# If the item exists, remove it and add a new one
if remove_item in grocery_list:
    grocery_list.remove(remove_item)
    new_item = input('Enter a new item to add to the list: ').title()
    grocery_list.append(new_item)
    print('\n✅ Update complete!')
else:
    print('\n⚠️ Item not found in the list.')

print(f'\n🛍️ Final Grocery List: {grocery_list}')
