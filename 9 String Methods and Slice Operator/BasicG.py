# Sentence Word Counter

# Input: A sentence from the user.

# Task:

# Remove commas and periods

# Convert to lowercase

# Count how many times the word "python" appears

# Print the count

sentence = input('Enter sentence: ').lower()

clean_sentence = sentence.strip(', .')
print(f" the word 'python' appears: {sentence.count('python')} times")
