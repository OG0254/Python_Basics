print("==== Simple POS System ====")

items = []        # To store all product details
grand_total = 0
item_number = 1

while True:
    print(f"\nProduct {item_number}")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    total = quantity * price
    grand_total += total

    # Save this item to the list
    items.append({
        'name': product_name,
        'quantity': quantity,
        'price': price,
        'total': total
    })

    more = input("Do you want to add another item? (yes/no): ")
    if more.lower() != 'yes':
        break
    item_number += 1

# Print final receipt
print("\n==== Final Receipt ====")
for item in items:
    print(f"{item['name']}: {item['quantity']} x Kes {item['price']} = Kes {item['total']}")

print(f"Grand Total: Kes {grand_total}")
