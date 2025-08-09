print('--- Age Category Checker ---\n')
age = float(input('Enter age: '))


if age >= 0 and age <= 12:
    print('Child')
else:
    if age >= 13 and age <= 17:
        print('Teenager')
    else:
        if age >= 18 and age <= 59:
            print('Adult')
        if age < 0:
            print('Age cannot be negative')
        else:
            print('senior')
