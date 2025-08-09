n = input('Enter a word: ')
vowel_count = 0

for letter in n:
    if letter.lower() in 'aeiou':
        vowel_count += 1

print(f"The number of vowels in '{n}' is {vowel_count}")
