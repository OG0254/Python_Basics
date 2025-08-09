def find_largest(numbers):
    """Find the largest number in a list."""  # when you have alot of numbers
    if not numbers:
        return None
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


print(find_largest([4, 9, 2]))


# OR


def find_largest(a, b, c):
    """Find the largest among three numbers."""  # when you have only three numbers
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


print(find_largest(4, 9, 2))
