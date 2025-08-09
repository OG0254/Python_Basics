print('--- Welcome to Python Bank 🏦 ---\n')

loop = True

# deposit = 0
# withdraw = 0
total = 10000

correct_pin = "1234"

# while loop:
for attempt in range(3):
    pin = (input('Enter your 4-digit PIN: '))
    if pin == correct_pin:
        print('Login successful')
        while loop:
            print('---- ATM ----')
            print('1.   Check balance')
            print('2.   Deposit')
            print('3.   Withdraw')
            print('4.   Exit')

            choice = input("Enter your choice (1/2/3/4): ")

            if choice == '1':
                print(f'Balance is: {total}')

            elif choice == '2':
                deposit = int(input('Enter amount to deposit: '))
                # total += deposit
                print(f'Deposit successful! New balance:{deposit + total}')

            elif choice == '3':
                withdraw = int(input('Enter amount to withdraw: '))
                if withdraw <= total:
                    total -= withdraw
                print(f'Withdrawal successful! New balance:{total - withdraw}')

            elif choice == '4':
                print('exit')
                break
    else:
        print('Invalid credentials access denied')
