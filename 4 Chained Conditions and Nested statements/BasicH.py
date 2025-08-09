print('--- Discount Calculator ---\n')
amount = float(input('Enter amount spent: '))

if amount >= 1000:
    print("Discount is 20%\n")
    print(f"Final price is: {amount * 0.80} \n")

if amount >= 500 and amount <= 999:
    print('Discount is 10%')
    print(f'Final price is: {amount * 0.90} \n')

else:
    print(f'No discount final price is: {amount} \n')
