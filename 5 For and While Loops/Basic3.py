print('--- Laundry Countdown Timer ---\n')

loop = True

minutes = int(input('How many minutes the laundry will take? '))
while loop:
    for x in range(minutes, 0, -1):
        print(f'\n🌀 Washing... {x} minutes remaining')

    print(f'\nWashing took {minutes} minutes to finish\n')
    break
