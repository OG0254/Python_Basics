# You have a list of brand names.
# Print out all the brands where:

# The first letter is a vowel (a, e, i, o, u)
# AND

# The name length is greater than 4 characters

brands = ['Oppo', 'Apple', 'Asus', 'Intel',
          'HP', 'Acer', 'Uber', 'Oracle', 'IBM']
for brand in brands:
    if brand[0].lower() in 'aeiou':
        if len(brand) > 4:
            print(brand)
