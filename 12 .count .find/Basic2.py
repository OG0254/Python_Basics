# Objective:

# Open and read a text file.

# Ask the user to input a word to search.

# Use .find() to locate the first position where that word appears.

# If the word is found, display the position (index); if not, tell the user it's not there.

# filename = input("Enter the filename to open: ")
filename = input("Enter the filename to open: ")
try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
    exit()
word = input("Enter a word to find: ")
position = content.find(word)
if position != -1:
    print(f"The word '{word}' is found at position {position}.")
else:
    print(f"The word '{word}' is not found in the file.")
