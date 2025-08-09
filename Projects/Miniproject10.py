secret_number = 7

while True:
    number = int(input("Guess the number: "))
    if number == secret_number:
        print("You got it!")
        break
    while True:
        if number > secret_number:
            print("Too high!")
        else:
            # while False:
            if number < secret_number:
                print("Too low!")
        break
