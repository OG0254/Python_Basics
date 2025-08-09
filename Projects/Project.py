print('--- Basic Budget Helper ---\n')

income = float(input('Enter monthly income: '))

expense = float(input('Enter expense amount: '))

savings = income - expense
savings_percent = (savings / income) * 100

if savings_percent >= 30:
    print(f"{savings_percent:.2f}% → You're saving well")
elif savings_percent >= 0:
    print(f"{savings_percent:.2f}% → Try to cut down on some expenses")
else:
    print("You're overspending, consider adjusting your budget")
