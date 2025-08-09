# You're building a login system that:

# Prompts the user for a password (correct one is python123)

# Allows only 5 attempts

# If correct, prints success message and number of attempts it took

# If not correct after 5 tries, prints: "Too many attempts. Access denied!"

print('--- Enhanced Password Validator ---\n')

loop = True
attempts = 0

while loop:
    password = input('Enter password: ').lower()
    attempts += 1
    if password == 'python123':
        print('Correct password ')
        print(f'It took {attempts} tries to get it right')
        break
    elif attempts == 5:
        print('Too many attempts. Access denied!')
        break
