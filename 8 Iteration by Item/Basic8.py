# Print the list of phones with their position numbers, but only if the phone name starts with a vowel.
phones = ['Samsung', 'Oppo', 'iPhone', 'Tecno', 'Infinix', 'Google']
for index, phone in enumerate(phones, start=1):
    if phone[0].lower() in 'aeiou':  # 0 means the 1st letter so it'll start from the 1st letter eg in samsung it'll start at S but if you put one it'll start with A
        print(f'{index} . {phone}')
