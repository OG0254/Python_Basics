print('--- 🛒 Simple Grocery Basket Checker Menu ---\n')

# 💡 Requirements:

# You're at a self-checkout counter. The system keeps asking you to enter the item name and price, '
# 'and it keeps tallying the total. When you're done, you type "done" and it gives you a receipt.
# Ask the user to enter item name and price.

# Keep adding items until they type 'done'.

# Show total number of items and the total cost.

print('--- 🛒 Simple Grocery Basket Checker Menu ---\n')

loop = True
total = 0
items = 0

while loop:
    item = input("Enter item name (or 'done' to finish): ").lower()

    if item == 'done':
        loop = False
        break

    try:
        price = float(input(f"Enter price for {item}: "))
        total += price
        items += 1
    except ValueError:
        print("Please enter a valid number for price.")

print(f'\n🧾 Receipt: \nTotal items: {items} \nTotal cost: Ksh {total}')

# OR

print('--- 🛒 Simple Grocery Basket Checker Menu ---\n')

loop = True
total = 0
items = 0

while loop:
    item = input("Enter item name (or 'done' to finish): ").lower()

    if item == 'done':
        loop = False
    else:
        price_input = input(f"Enter price for {item}: ")

        if price_input.isdigit():
            price = int(price_input)
            total += price
            items += 1
        else:
            print("Invalid price! Please enter numbers only.")

print(f'\n🧾 Receipt: \nTotal items: {items} \nTotal cost: Ksh {total}')


# OR

print('--- 💰 Grocery Basket (No Validation) ---\n')

total = 0
items = 0

while True:
    item = input("Enter item name (or 'done' to finish): ").lower()

    if item == 'done':
        break

    price = float(input("Enter price: "))
    total += price
    items += 1

print(f'\n🧾 Receipt:')
print(f'Total items: {items}')
print(f'Total cost: Ksh {total}')
