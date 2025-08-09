# a simple admin mode — so if you login with username admin and a special password, you can view all accounts.


accounts = {
    "ogada": "Valid2",
    "brian": "Valid1",
    "admin": "superpass"
}

print('--- Simple Login System ---\n')

while True:
    username = input('Enter username: ').strip().lower()

    if username not in accounts:
        print('Check username and try again.\n')
        continue

    # If username is admin, ask for password and show accounts
    if username == "admin":
        admin_password = input("Enter admin password: ")
        if accounts["admin"] == admin_password:
            print("\n--- All Registered Accounts ---")
            for user, pwd in accounts.items():
                print(f"Username: {user}, Password: {pwd}")
            print("\nExiting system.")
            break
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

    print('Too many failed attempts. Account locked.')

    reset_choice = input(
        "Do you want to reset your password? (yes/no): ").lower()

    if reset_choice == "yes":
        new_password = input("Enter new password: ")
        confirm_password = input("Confirm new password: ")

        if new_password == confirm_password:
            accounts[username] = new_password
            print("Password reset successfully! 🎉 You can now login again.\n")
        else:
            print("Passwords do not match. Reset failed.\n")
    else:
        print("Goodbye.")
        break
