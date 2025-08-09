# Next move:
# Let’s try adding a simple condition inside the loop — for example:
# Print only the animals whose names start with 'C'.

animals = ['Parrot', 'Eagle', 'Cow', 'Chicken']
for animal in animals:
    if animal.endswith('w') or animal.endswith('W'):
        print(animal.upper())  # prints the name in all UPPERCASE
