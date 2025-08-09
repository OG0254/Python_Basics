number = int(input("Enter number: "))

if number in range(1, 51):
    print("Within 1 to 50")
elif number in range(51, 101):
    print("Within 51 to 100")

else:
    print("Out of range")
