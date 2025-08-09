print('--- Expense Tracker ---\n')

total = 0
high_spending_days = 0  # Track days over 1000

for x in range(1, 8):
    expenses = float(input(f'Enter expenses for Day {x}: '))
    total += expenses
    if expenses > 1000:
        high_spending_days += 1

average_spending = total / 7

print(f'\nTotal amount spent: {total}')
print(f'Average daily spending: {average_spending:.2f}')
print(f'Days you spent more than 1000: {high_spending_days}')
