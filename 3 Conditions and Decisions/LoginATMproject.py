# Write a program that:

# Asks the user for a number
# Checks whether it’s Even or Odd (Hint: use number % 2 == 0)

# Code

# num = int(input('Enter a number: '))

# if num % 2 == 0:
#    print('Even')

# else:
#    print('Odd')

# Login system

# Ask the user to enter a username and password
# Check if they match the correct username and password
# If correct → print “Login successful”
# If not → print “Invalid credentials”
# You can assume:

# Correct username = "admin"
# Correct password = "1234"

user_name = input("Enter Username: ")
password = input("Enter password: ")

if user_name == "admin" and password == "1234":
    print("Login successful")

    print("---- ATM ----")
    print("1.   Check balance")
    print("2.   Withdraw")
    print("3.   Deposit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        print("Check balance")

    elif choice == "2":
        print("Withdraw")

    elif choice == "3":
        print("Deposit")

    else:
        print("Invalid choice")


else:
    print("Invalid credentials access denied")


# Research more
