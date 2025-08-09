num = int(input('Enter a number: '))
for x in range(1, 1 + num):
    if x % 2 == 0:
        print(f'{x} squared is {x ** 2}')
    if x % 2 != 0:
        print(f'{x} cubed is {x ** 3}')


# num = int(input('Enter a number: '))
# for x in range(1, 1 + num):
# else:
    # if x % 2 != 0:
    # print(f'{x} cubed is {x ** 3}')
