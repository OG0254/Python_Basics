# You are building a system that keeps asking the user to enter a password until they enter the correct one.

# Requirements:
# The correct password is "python123".

# Keep asking until the correct password is entered.

# Count how many attempts it took.

# Print a success message and number of attempts once they get it right.

print('--- Simple Password Validator ---\n')

loop = True
attempts = 0

while loop:
    password = input('Enter password: ').lower()
    attempts += 1
    if password == 'python123':
        print('Correct password ')
        print(f'It took {attempts} tries to get it right')
        break
