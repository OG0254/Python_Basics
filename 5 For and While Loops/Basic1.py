loop = True

num = int(input('Enter a number: '))
total = 0
while loop:
    for x in range(num, 0, - 1):
        total += x
        print(x)
        loop = False
    print('Blast off! 🚀')
