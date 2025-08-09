# Challenge:
# You have this list of phone brands:
# Task:
# 👉 Print out only the phones where the last letter is a vowel (A, E, I, O, U — upper or lowercase).
# 👉 Print them in uppercase too.

phones = ['Samsung', 'Oppo', 'iPhone', 'Tecno', 'Infinix', 'Google']
for index, phone in enumerate(phones, start=1):
    if phone[-1].lower() in 'aeiou':  # 0 means the 1st letter so it'll start from the 1st letter eg in samsung it'll start at S but if you put one it'll start with A
        print(f'{index} . {phone.upper()}')
