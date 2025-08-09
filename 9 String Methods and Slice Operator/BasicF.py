# Email Validator (Basic)

# Input: User enters an email address.

# Task:

# Remove leading and trailing spaces

# Check if it contains "@" and "."

# If both exist, print Valid Email

# Else, print Valid Email

print("-- Email Validator --\n")

email = input("Enter email adsress: ").strip()

if "@" in email and "." in email:
    print("Valid Email")

else:
    print("Invalid Email")
