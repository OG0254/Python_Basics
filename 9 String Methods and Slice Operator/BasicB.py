# Name Formatter
# Input: A user’s full name (first and last) with random spaces before/after and messy casing.
# Task:

# Remove extra spaces

# Capitalize the first letter of each name

# Print a greeting like: Hello, First Last!

print('--- Name Formatter ---\n')

details = input('Enter Full Name: ').title()
print(f'Hello, {details.strip()}!')
