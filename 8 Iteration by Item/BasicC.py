# From the same list, print only the items that start with the letter 'C'.

print('--- Basic List Iteration ---\n')

food = ['Pizza', 'Chicken', 'Rice', 'Chapati']
for x in food:
    if x.startswith('c') or x.startswith('C'):
        print(x)
