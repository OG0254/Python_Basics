# Write a small Python program that:

# Takes a string input from the user

# Converts it to uppercase

# Replaces all spaces with underscores _

# Prints out the modified string and the number of characters in it

text = input('Enter your text: ')
new_text = text.upper(). replace(' ', '_')
print(
    f'modified string: {new_text}, the number of characters: {len(new_text)}')
