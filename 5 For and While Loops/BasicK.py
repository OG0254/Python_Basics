num = int(input('Enter a number: '))
for x in range(1, 1 + num):
    if x % 2 != 0:
        print(f'{x ** 3}')
