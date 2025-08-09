print("Mobile Airtime Top-up Project\n")

starting_balance = 2000
current_balance = starting_balance
total_used = 0
# new_balance = 0
while True:
    phone_number = int(input("Enter phone number to top up: "))
    amount = int(input("Enter amount to top up: "))
    if amount > 10 and amount <= 1000:
        current_balance = current_balance - amount
        print(f"Balance is {current_balance}")
        # print(f"Balance is {current_balance}")
        # new_balance = current_balance - amount
        total_used = starting_balance - current_balance
    else:
        print("Amount top up not allowed")
        # break
    more = input("Do you want to add another top up? (yes/no): ")
    if more.lower() != "yes":
        break
print(f"Total amount used: Kes {total_used}")
