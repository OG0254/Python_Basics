text = input('Username: ')
try:
    number = int(text)
    print(number)
except ValueError:
    print('Invalid username')
    
