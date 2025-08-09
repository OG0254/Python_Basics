#  Iteration by Item Challenge
# Challenge:

# Create two lists: one with food items and another with their matching prices.

# Loop through both lists.

# Display each food item with its price.

# Calculate the total bill as you loop.

# Finally, print a clean receipt showing:

# List of items with prices.

# Total bill at the bottom.

print('--- Iteration by Item ---\n')

price = 0

total = 0

foods = ['Banana', 'Apple', 'Pear', 'Chicken', 'Fish']

prices = [10, 30, 20, 100, 200]

# here the key is prices the value is foods

for x in range(len(foods)):
    total += prices[x]
    print(f'{foods[x]} - {prices[x]} KES')
    print(f'{total} KES\n')
print(f'Total bill : {total} KES')
