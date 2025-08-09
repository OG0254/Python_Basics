def Simple_Inventory_management_system():
    inventory = {}

    def add_item(item_name, quantity):
        if item_name in inventory:
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity

    def remove_item(item_name, quantity):
        if item_name in inventory and inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            if inventory[item_name] == 0:
                del inventory[item_name]
        else:
            print("Item not found or insufficient quantity.")

    def view_inventory():
        if not inventory:
            print("Inventory is empty.")
        else:
            for item, quantity in inventory.items():
                print(f"{item}: {quantity}")

    while True:
        print("\nSimple Inventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Search Item by Name")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item_name, quantity)
            print(f"Added {quantity} of {item_name} to the inventory.")
        elif choice == "2":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            remove_item(item_name, quantity)
            print(f"Removed {quantity} of {item_name} from the inventory.")
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            item_name = input("Enter item name to search: ")
            if item_name in inventory:
                print(
                    f"{item_name} is in the inventory with quantity {inventory[item_name]}."
                )
            else:
                print(f"{item_name} is not found in the inventory.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


# Call the function to run the inventory management system
Simple_Inventory_management_system()
