# Challenge:
# You have a list of country names.

# Task:
# Print the countries that:

# Start with a vowel (a, e, i, o, u)

# End with the letter 'a'

# Have a name length of at least 5 characters

countries = ['Algeria', 'Uganda', 'India', 'Oman', 'Eritrea',
             'Argentina', 'Iceland', 'Estonia', 'Uruguay', 'Angola']

for index, country in enumerate(countries, start=1):
    if country[0].lower() in ('aeiou'):
        if country.endswith('a'):
            if len(country) >= 5:
                print(f'{index}. {country}')
print('...')
