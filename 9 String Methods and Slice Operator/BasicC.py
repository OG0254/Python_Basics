# Word Counter
# Input: A sentence from the user.
# Task:

# Count how many times the word "python" appears (case insensitive)

# Print the count

print('--- Word Counter ---\n')

information = input('Enter sentence: ').lower()
words = information.split()
print(f"{words.count('the')}")
