# Assignment:
# Ask the user to enter a word.
# Then:

# Print the word reversed.

# Print every second letter from the word.

# Print the word without the first and last character.

full_word = input('Enter word to use: ')

print(full_word[::-1])
print(full_word[::2])  # word[::2] → every 2nd letter starting at index 0
print(full_word[1::2])  # every 2nd letter starting at index 1
print(full_word[1:-1])
