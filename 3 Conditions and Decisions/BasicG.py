print('\n--- Simple Loan Calculator ---')
amount = float(input('Enter loan amount: '))
interest = float(input('Enter interest rate: '))
term = float(input('Enter loan term: '))
r = (interest / 100) / 12
n = term * 12
payment = (amount * r * (1 + r) ** n) / ((1 + r) ** n - 1)
print(f'''
Loan amount is: {amount}
Interest rate is: {interest} %
Loan term is: {term}
Monthly payment is: {payment} ''')
