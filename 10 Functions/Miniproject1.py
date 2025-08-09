def shoppingcart_system():
    cart = []
    while True:
        print("Welcome to the Shopping Cart System!")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Please select an option (1-5): ")

        if choice == "1":
            item = input("Enter the item you want to add: ")
            cart.append(item)
            print(f"{item} has been added to your cart.")

        elif choice == "2":
            item = input("Enter the item you want to remove: ")
            if item in cart:
                cart.remove(item)
                print(f"{item} has been removed from your cart.")
            else:
                print(f"{item} is not in your cart.")

        elif choice == "3":
            if cart:
                print("Your cart contains:")
                for i, item in enumerate(cart, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your cart is empty.")

        elif choice == "4":
            if cart:
                total_items = len(cart)
                print(f"You have {total_items} items in your cart.")
                print("Thank you for shopping with us!")
                break
            else:
                print("Your cart is empty. Please add items before checking out.")

        elif choice == "5":
            print("Exiting the Shopping Cart System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    shoppingcart_system()
