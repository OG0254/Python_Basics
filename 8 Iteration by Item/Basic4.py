# You have a list of fruits. Print out only those fruits whose names have more than 5 characters.

fruits = ['Banana', 'Kiwi', 'Watermelon', 'Apple', 'Orange']
for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)
