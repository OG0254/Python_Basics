def num_checker(numbers):
    """Check if the numbers are even or odd."""
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")


num_checker([1, 2, 3, 4, 5])
