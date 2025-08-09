# Example
# Write a Python program that:

# Asks the user to enter two numbers.
# Perform and display the results of:
# Addition
# Subtraction
# Multiplication
# Division


# Code A

# print('--- Simple Calculator---')

# a = float(input('Enter number 1: '))
# b = float(input('Enter number 2: '))

# print('Addition', a + b) 
# print('Subtraction', a - b)
# print('Multiplication',  a * b) 
# print('Division',  a / b)



# Write a program that:

# Asks the user to enter two numbers
# Shows a menu of operations:
# Press 1 for Addition
# Press 2 for Subtraction
# Press 3 for Multiplication
# Press 4 for Division
# Based on the user’s choice, perform the corresponding operation and show the result.


# Code

# print('--- Simple Calculator ---')

# Input numbers
# a = float(input('Enter number 1: '))
# b = float(input('Enter number 2: '))

# Operation menu
# print("\nSelect Operation:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# User chooses operation
# choice = (input("Enter your choice (1/2/3/4): ")

# Perform selected operation
# if choice == '1':
#    print("Result: ", a + b)
# elif choice == '2':
#    print("Result: ", a - b)
#elif choice == '3':
#    print("Result: ", a * b)
#elif choice == '4':
#    if b != 0:
#        print("Result: ", round(a / b, 2)) # this is the same as division
#    else:
#        print("Error: Cannot divide by zero!") # the best since if you divide a number by zero the code won't give an error but it will print out the statement given
    
    # print("Result: ", a / b) # issue with this we sahll get an error if we didvide the number by zero thus breaking the code
# else:
#    print("Invalid choice! Please select 1, 2, 3, or 4.")


# When you want the user to to do more than one calculation you add the while function before the fuctions

# Code

print('--- Simple Calculator ---')

while True:
    # Input numbers
    a = float(input('Enter number 1: '))
    b = float(input('Enter number 2: '))

    # Operation menu
    print("\nSelect Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # User chooses operation
    choice = input("Enter your choice (1/2/3/4): ")

    # Perform selected operation
    if choice == '1':
        print("Result:", a + b)
    elif choice == '2':
        print("Result:", a - b)
    elif choice == '3':
        print("Result:", a * b)
    elif choice == '4':
        if b != 0:
            print("Result:", round(a / b, 2))
        else:
            print("Error: Cannot divide by zero!")
    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")

    # Ask if user wants to continue
    again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print("Thanks for using the calculator. Goodbye!")
        break

