# Extract Middle Characters
# Ask the user to enter a word.
# Then, using slicing, print:

# The first 3 characters

# The last 3 characters

# The middle character(s) (if the word length is odd, show 1 middle character — if even, show 2 middle characters)

text = input('Enter a word: ')
print(text[:3])
print(text[-3:])

# Get the length of the text
length = len(text)

# Calculate the middle index
middle_index = length // 2

# Check if the length is even or odd
if length % 2 == 0:
    print(f"Middle characters: {text[middle_index-1:middle_index+1]}")
else:
    print(f"Middle character: {text[middle_index]}")
