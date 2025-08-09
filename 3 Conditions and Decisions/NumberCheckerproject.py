# Number checker
# Write a program that:

# Takes a number from the user
# Checks and prints if it is:
# Positive
# Negative
# Zero

num = int(input('Enter a number: '))

if num >= 1:
    print('Positive')

elif num <= -1:
    print('Negative')

else:
    print('Zero')