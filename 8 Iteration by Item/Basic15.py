# You have this list of words:
# Task:

# Print all words that:

# Start with a vowel (A, E, I, O, U)

# End with the letter e

# Have more than 6 letters

words = ['Application', 'Orange', 'Elegant', 'Idea',
         'Oasis', 'Example', 'Update', 'Indigo', 'Option']
for index, word in enumerate(words, start=1):
    if word[0].lower() in ('aeiou'):
        if word.endswith('e'):
            if len(word) > 6:
                print(f'{index}. {word}')
