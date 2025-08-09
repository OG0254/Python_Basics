#  allow user to enter the current_year

name = str(input('Enter your name: '))
birth_year = int(input('Enter your birth year: '))
current_year = int(input('Enter current year: '))

birth_year = current_year - birth_year



print('\n---- Summary of name and age ---')
print(f'{name}')
print(f'{birth_year}')
print(f'In 10 years you will be {birth_year + 10}')

if birth_year >= 18:
    print('You are an adult')

else:
    birth_year < 18
    print('You are a minor')