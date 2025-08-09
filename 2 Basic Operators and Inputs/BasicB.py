print('\n--- Weekly Salary Calculator ---')
name = input('Enter your name : ')
hours = float(input('Enter hours worked : '))
rate = float(input('Enter rate per hour : '))
salary = hours * rate

print('\n--- Salary Slip ---')
print(f'Name : {name} \n')
print(f'Hours Worked : {hours} \n')
print(f'Rate per Hour : {rate} \n')
print(f'Weekly Salary : {salary}')
