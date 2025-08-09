print('--- Student Score Tracker ---\n')

total = 0

tests = int(input(f'How many tests have you done? '))

for x in range(1, tests + 1):

    score = float(input(f'Enter score for {x}: '))

    total += score  # total = total + score

    average = total / tests

print('--- Final scoring ---\n')
print(f'Total score is:{total} ')
print(f'Average score is:{average} ')

if average >= 80:
    print('Well done! Keep it up 👍')
elif average >= 50:
    print("You're doing okay, but there's room to improve")
else:
    print('You need to work harder 💪')
