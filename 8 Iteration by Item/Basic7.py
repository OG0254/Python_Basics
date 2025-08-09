# Challenge:
# You have a list of phone brands. Print only the brands that have more than 6 letters in their name, and print them in uppercase.

phones = ['Samsung', 'Oppo', 'iPhone', 'Tecno', 'Infinix', 'Google']
for phone in phones:
    if len(phone) > 6:
        print(phone.upper())
