# Using enumerate()
# we add numbering while iterating.
# enumerate() gives us both:

# the index (position)

# the item itself

# Assignment
# Rewrite your animals list loop using enumerate() and number the animals when printing.

animals = ['Parrot', 'Eagle', 'Cow', 'Chicken']
for index, animal in enumerate(animals, start=1):
    print(f'{index} . {animal}')
