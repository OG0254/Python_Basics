print('--- Exam Score ---\n')
grade = float(input('Enter grade: '))

if grade > 0:
    if grade >= 90:
        if grade == 100:
            print('Perfect score!')
        else:
            print('Excellent work!')
    else:
        if grade >= 80:
            print('Good job!')
        else:
            if grade >= 70:
                print('You passed, but you can do better.')
            else:
                if grade >= 50:
                    print('You need to work harder.')
                else:
                    print("You failed. Let's study more!")
else:
    print('Please be more serious, this is your life.')
