# Challenge:
# You have a list of brand names. Print only the brands that:

# Start with a vowel (a, e, i, o, u)
# AND

# End with the letter 'e'

brands = ['Apple', 'Orange', 'Intel', 'Oracle',
          'Acer', 'Uber', 'Asus', 'Oppo', 'Adobe']
for index, brand in enumerate(brands, start=1):
    if brand[0].lower() in ('aeiou'):
        if brand.endswith('e'):
            print(f'{index}. {brand}')
