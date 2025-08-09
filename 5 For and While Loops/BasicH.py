num = int(input('Enter a number: '))
for x in range(1, num + 1):
    if x % 2 == 0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')
