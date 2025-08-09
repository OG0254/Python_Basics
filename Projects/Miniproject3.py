# upgrade with add & delete options for admin! 🔥

accounts = {
    "ogada": "Valid2",
    "brian": "Valid1",
    "admin": "superpass"
}


def show_accounts():
    print("\n--- All Registered Accounts ---")
    for user, pwd in accounts.items():
        print(f"Username: {user}, Password: {pwd}")


def add_account():
    new_user = input("Enter new username: ").lower()
    if new_user in accounts:
        print("User already exists.")
    else:
        new_pass = input("Enter new password: ")
        accounts[new_user] = new_pass
        print(f"Account '{new_user}' added successfully!")


def delete_account():
    del_user = input("Enter username to delete: ").lower()
    if del_user == "admin":
        print("Cannot delete admin account.")
    elif del_user in accounts:
        del accounts[del_user]
        print(f"Account '{del_user}' deleted successfully!")
    else:
        print("User not found.")


print('--- Simple Login System ---\n')

while True:
    username = input('Enter username: ').strip().lower()

    if username not in accounts:
        print('Check username and try again.\n')
        continue

    # If admin logs in
    if username == "admin":
        admin_password = input("Enter admin password: ")
        if accounts["admin"] == admin_password:
            print("\nWelcome, Admin!")
            while True:
                print("\nChoose an action:")
                print("1. Show all accounts")
                print("2. Add new account")
                print("3. Delete an account")
                print("4. Logout")

                choice = input("Select option (1-4): ")

                if choice == "1":
                    show_accounts()
                elif choice == "2":
                    add_account()
                elif choice == "3":
                    delete_account()
                elif choice == "4":
                    print("Logging out of admin mode.\n")
                    break
                else:
                    print("Invalid option.")
            continue
        else:
            print("Wrong admin password.\n")
            continue

    # Regular user login
    attempts = 3
    while attempts > 0:
        password = input('Enter password: ')

        if accounts[username] == password:
            print('Login successfully 🎉')
            exit()

        else:
            attempts -= 1
            print(f'Wrong password. {attempts} attempts remaining.')

    print('Too many failed attempts. Account locked.\n')
    break
