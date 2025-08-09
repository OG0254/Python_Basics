print('\n--- Age in Months, Weeks, and Days ---')
years = int(input('Enter your age in years: '))
months = years * 12
weeks = years * 52
days = years * 365
print('\n--- Summary of Age ---')
# print(f'You are: \n-{years} years old \n-{months} months old \n-{weeks} weeks old \n-{days} days old')
print(f'''
You are: 
-{years} years old 
-{months} months old 
-{weeks} weeks old 
-{days} days old''')
