print('\n--- Movie Ticket Pricing Based on Age ---')
age = int(input('Enter your age: '))
if age >= 60:
    print('You are a senior citizen.')
    print('Your movie ticket price is: 6 USD')
elif age >= 20:
    print('You are a adult.')
    print('Your movie ticket price is: 10 USD')
elif age >= 13:
    print('You are a teenager.')
    print('Your movie ticket price is: 5 USD')
elif age >= 0:
    print('You are a kid.')
    print('Your movie ticket price is: Free 🎉')
else:
    print('You are an alien')
