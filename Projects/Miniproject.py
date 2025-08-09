# Simple Login System
# Concept:

# User creates a username and password.

# Then they're asked to log in.

# Program checks if the entered details match.

# If yes → "Login successful"

# If not → "Invalid credentials"

# usernames = 'Ogada', 'Brian'
# passwords = 'valid2', 'Valid1'

accounts = {
    "ogada": "Valid2",
    "brian": "Valid1"
}

print('--- Simple Login System ---\n')

while True:
    username = input('Enter username: ').strip().lower()

    if username not in accounts:
        print('Check username and try again.\n')
        continue

    # If username is correct, give 3 password attempts
    attempts = 3
    while attempts > 0:
        password = input('Enter password: ')

        if accounts[username] == password:
            print('Login successfully 🎉')
            exit()

        else:
            attempts -= 1
            print(f'Wrong password. {attempts} attempts remaining.')

    # After 3 failed attempts, offer to reset password
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
