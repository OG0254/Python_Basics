# Collect student details and exam score.
# Determine the grade using chained conditions.
# Use nested if statements to decide if the student passed or failed, and give feedback.

# Code

print('\n--- Students Score ---')

name = input('Enter student name: ')
score = int(input('Enter score: '))

print('\n--- Feedback ---')
print(f'Student name: {name}')
print(f'Student score: {score}')

if score > 80:
    print(f'{name} passed')

else:
    print(f'{name} failed')

