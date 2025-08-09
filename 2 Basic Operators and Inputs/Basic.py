print('Daily Expenses Calculator\n')
# print('Breakfast: ')
Breakfast = float(input('Enter cost of breakfast : \n'))
# print('Lunch: ')
Lunch = float(input('Enter cost of lunch : \n'))
# print('Transport: ')
Transport = float(input('Enter cost of transport : \n'))
# print('Snacks: ')
Snacks = float(input('Enter cost of snacks : '))

Total_Spent = Breakfast + Lunch + Transport + Snacks

print('--- Daily Expense Summary ---')
print(f'Breakfast : {Breakfast}')
print(f'Lunch : {Lunch}')
print(f'Transport : {Transport}')
print(f'Snacks : {Snacks}')
print(f'Total Spent Today : {Total_Spent}')
