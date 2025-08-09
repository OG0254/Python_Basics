# Sentence Cleaner
# Input:
# A sentence from the user with random commas, periods, and extra spaces.

# Task:

# Remove all commas and periods

# Convert the whole sentence to lowercase

# Split it into words

# Print the cleaned list of words

senstence = input(
    'User enter sentence with random coomas, periods and extra spaces: ').replace(',', '').replace('.', '').lower()
word = senstence.split()
print(f'Cleaned verion is: {word}')
