# Create a list of your 5 favorite cities, then use a for loop to print them out numbered nicely like:

# markdown
# Copy
# Edit
# 1. Nairobi
# 2. Mombasa
# 3. Kigali
# ...

print('--- Favorite Cities ---\n')

cities = ['Nairobi', 'Mombasa', 'Kigali']
for index, city in enumerate(cities, start=1):
    print(f'{index}. {city}')
print('...')
