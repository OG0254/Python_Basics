print('--- Simple Calculator with Conditions ---\n')
num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))
operation = input('Enter operation? ').lower()

if operation == 'add':
    print(f'{num1 + num2}')
if operation == 'subtract':
    print(f'{num1 - num2}')
if operation == 'multiply':
    print(f'{num1 * num2}')
if operation == 'divide':
    print(f'{num1 / num2}')

else:
    print('Invalid operation, please choose add, subtract, multiply, or divide')
# + , - , * , /
