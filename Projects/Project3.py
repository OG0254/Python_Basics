print("Welcome to Ogada's Mini Store Inventory\n")

print("1. View Stock ")
print("2. Sell Item ")
print("3. Restock Item ")
print("4. Exit ")

stock_name = ["Water", "Soda", "Snacks"]
stock_amount = [10, 5, 20]
while True:
    choice = int(input("Enter choice 1/2/3/4: "))
    if choice == 1:
        # print(list(zip(stock_name, stock_amount)))
        for name, amount in zip(stock_name, stock_amount):
            print(name, amount)

    elif choice == 2:
        while True:
            item_name = str(input("Enter the item name: ")).strip().title()
            if item_name in stock_name:
                index = stock_name.index(item_name)
            else:
                print("Item not available")
                break
            amount = int(input("Enter how pieces you want to sell: "))
            if stock_amount[index] >= amount:
                new_total = stock_amount[index] - amount
                stock_amount[index] -= amount
                print(f"New total amount is {new_total}")
                # balance = stock_amount[index] - amount
                # print(balance)
                print("Sale confirmed!")
            else:
                print("Insufficient stock")
            more = input("Do you want to sell another item? (yes/no) ")
            if more.lower() != "yes":
                print("New stock after sell: ")
                for name, amount in zip(stock_name, stock_amount):
                    print(name, amount)
                print("\nUser logged out!\n")
                break

    elif choice == 3:
        while True:
            item_name = str(input("Enter the item name: ")).strip().title()
            if item_name in stock_name:
                index = stock_name.index(item_name)
            else:
                print("Item not available")
                break
            amount = int(input("Enter how pieces you want to add: "))
            # if stock_amount[index] >= amount:
            new_total = stock_amount[index] + amount
            stock_amount[index] += amount
            # balance = stock_amount[index] - amount
            # print(balance)
            print(f"New total amount is {new_total}")
            print("Addition confirmed!")
            more = input("Do you want to add another item? (yes/no) ")
            if more.lower() != "yes":
                print("New stock after addition: ")
                for name, amount in zip(stock_name, stock_amount):
                    print(name, amount)
                print("\nUser logged out!\n")
                break

    else:
        choice == 4
        print("See you soon!")
        break
