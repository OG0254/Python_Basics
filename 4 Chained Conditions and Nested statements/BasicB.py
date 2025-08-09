print('--- Travel Destination Suggestion ---\n')
# helps with case senstive issues example YES or YeS or yes or NO or nO
query = str(input('Ask user if they have a passport: ')).strip().lower()
# age = int(input('Enter age: '))

if query == 'yes':
    # this helps with when the users says no it just terminates the code and prints whar after the else
    age = int(input('Enter age: '))
    if age >= 18:
        print("You're good to travel abroad!")
    else:
        print("You’ll need parental guidance to travel.")
else:
    print("You need a passport to travel, no matter your age.")
