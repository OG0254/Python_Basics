# Password Masker
# Input: A password from the user.
# Task:

# Replace all characters with *

# Print how many characters the password had

password = input('Enter password: ')
hidden_password = '*' * len(password)
print(
    f"Password is: {hidden_password}, number of password characters: {len(password)}")
