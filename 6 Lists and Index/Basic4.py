# Task:

# Ask the user to enter an item name.

# If it exists, print all the positions where it appears in the list.

# If not, print "Item not found".

items = ["Pen", "Notebook", "Eraser", "Pencil", "Notebook"]

choice = str(input("Enter item name: ")).strip().title()
for index, item in enumerate(items):
    if choice in items:
        index = items.index(choice)
        count = items.count(
            choice
        )  # pointer on this code is  gives the number of times it appears what you entered
        print(count)

    else:
        print("Item not found")

# OR

items = ["Pen", "Notebook", "Eraser", "Pencil", "Notebook"]

choice = input("Enter item name: ").strip().title()

positions = []  # to store positions

for index, item in enumerate(items):
    if item == choice:
        positions.append(index)
        # pointer collect positions where the input matches.
if positions:
    print(f"{choice} found at positions: {positions}")
else:
    print("Item not found")
