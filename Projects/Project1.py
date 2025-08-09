print("--- Expense Tracker ---\n")
income = float(input("Enter monthly income: "))
expense_rent = float(input("Enter rent expense: "))
expense_food = float(input("Enter food expense: "))
expense_transport = float(input("Enter transport expense: "))
expense_clothing = float(input("Enter clothing expense: "))
expense_others = float(input("Enter other expenses: "))

Total_expenses = (
    expense_rent + expense_clothing + expense_food + expense_transport + expense_others
)

savings = income - Total_expenses
savings_percentage = (savings / income) * 100

# print('\n--- Detailed Expenses ---')
# print(f'Total income: {income}')
# print(f'Total expenses: {total_expenses}')
# print(f'Savings amount: {savings}')
# print(f'Savings percent: {savings_percentage:.2f}%')

print("--- Detailed Expenses ---\n")

if savings_percentage >= 30:
    print(f"Total income: {income}")
    print(f"Total expenses: {Total_expenses}")
    print(f"Savings amount: {savings}")
    print(f"{savings_percentage:.2f}% → You're saving well")
elif savings_percentage >= 0:
    print(f"Total income: {income}")
    print(f"Total expenses: {Total_expenses}")
    print(f"Savings amount: {savings}")
    print(f"{savings_percentage:.2f}% → Try to cut down on some expenses")
else:
    print("You're overspending, consider adjusting your budget")
