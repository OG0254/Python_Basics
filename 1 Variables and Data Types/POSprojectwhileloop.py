print("==== Simple POS System ====")

grand_total = 0
item_number = 1  # To count products

while True:
    print(f"\nProduct {item_number}")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))
    total = quantity * price
    grand_total += total

    print(f"{product_name}: {quantity} x Kes {price} = Kes {total}")

    more = input("Do you want to add another item? (yes/no): ")
    if more.lower() != 'yes':
        break
    item_number += 1

# Final receipt
print("\n==== Final Receipt ====")
print(f"Total amount to be paid: Kes {grand_total}")
