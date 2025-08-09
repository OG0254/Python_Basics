# Now take the same list, and print it with numbers like this:

# 1. Pizza
# 2. Chicken
# 3. Rice
# 4. Chapati

print('--- Basic List Iteration ---\n')

food = ['Pizza', 'Chicken', 'Rice', 'Chapati']
for index, x in enumerate(food, start=1):
    print(f'{index}. {x}')
