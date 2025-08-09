# # Challenge:
# # You have this list of countries
# Task:
# Print only the countries that start with the letter 'A' (whether uppercase or lowercase), and display them in uppercase.

countries = ['Kenya', 'Uganda', 'Algeria', 'Angola', 'South Africa', 'Rwanda']
for country in countries:
    if country.startswith('A') or country.startswith('a'):
        print(country.upper())
