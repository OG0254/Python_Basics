print('\n--- Grade Checker ---')
score = float(input('Enter your exam score: '))
if score >= 90:
    print('Your grade is: A')
elif score >= 80:
    print('Your grade is: B')
elif score >= 70:
    print('Your grade is: C')
elif score >= 60:
    print('Your grade is: D')
elif score >= 1:
    print('Your grade is: F')
else:
    print('Try better next time')
