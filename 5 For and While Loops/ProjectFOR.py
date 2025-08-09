print('--- Simple Loan Repayment Calculator ---\n')

loan = float(input('Enter loan amount: '))
annual_rate = float(input('Enter annual interest rate (%): '))
months = int(input('Enter loan term (in months): '))

monthly_rate = annual_rate / 12 / 100
monthly_payment = (loan * monthly_rate) + (loan / months)

total_repayment = 0
total_interest = 0

print('\n--- Monthly Repayment Schedule ---')
for month in range(1, months + 1):
    interest = (loan * monthly_rate)
    principal = loan / months
    payment = principal + interest

    total_interest += interest
    total_repayment += payment

    print(f'Month {month}: Ksh {payment:.2f}')

print('\n--- Summary ---')
print(f'Loan amount: Ksh {loan:.2f}')
print(f'Total interest: Ksh {total_interest:.2f}')
print(f'Total repayment: Ksh {total_repayment:.2f}')
