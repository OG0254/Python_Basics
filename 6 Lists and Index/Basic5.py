# Task:

# Ask the user to enter a device name.

# If it exists in the list, print all positions (indexes) where it appears.

# If not, print "Device not found".

devices = ["Phone", "Laptop", "Tablet", "Laptop", "Smartwatch"]

choice = input("Enter item name: ").strip().title()

positions = []  # to store positions

for index, item in enumerate(devices):
    if item == choice:
        positions.append(index)
        # pointer collect positions where the input matches.
if positions:
    print(f"{choice} found at positions: {positions}")
else:
    print("Device not found")
