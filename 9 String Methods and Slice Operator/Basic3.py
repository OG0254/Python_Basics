# Slicing + Condition Challenge
# Prompt:
# Ask the user to enter a word.

# If the word is longer than 5 characters, print the middle 3 characters.

# If it's 5 characters or fewer, print the word reversed.

word = input("Enter word: ")
# for word in words:
if len(word) > 5:
    middle_word = word[(len(word) // 2) - 1 : (len(word) // 2) + 2]
    print(middle_word)
else:
    print(word[::-1])
