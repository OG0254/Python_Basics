amount = int(input("Enter an amount: Kes "))
rate = amount / 130

if amount >= 1:
    print("Exchange rate is 1 USD = 130 Kes\n")
    print(f"USD value is {rate:.2f}USD")

else:
    print("Check amount and try again")
