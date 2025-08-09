# Name Initials Extractor

# Input: User enters their full name.

# Task:

# Remove extra spaces

# Capitalize each name

# Print the initials (first letter of each name)

full_name = input('Enter full name: ')
names = full_name.split()
initials = ".".join([name[0].upper() for name in names])
print(initials)
