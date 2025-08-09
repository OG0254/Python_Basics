# Task:

# Ask the user to enter a color.

# If the color is in the list, print its index.

# If not, print "Color not found".

colors = ["Red", "Green", "Blue", "Yellow", "Green"]

choice = input("Enter color of preference: ").strip().title()
# position = colors.index(choice)
if choice in colors:
    index = colors.index(choice)
    print(index)

else:
    print("Color not found")
