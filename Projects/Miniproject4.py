# simple login system first, then gradually add features like:

# ✅ Correct login checks
# ✅ Password mismatch warning
# ✅ Option to reset password
# ✅ Option to register a new user

accounts = {
    "Ogada": "Valid1",
    "Brian": "Valid2"
}
print('--- Login System ---\n')

while True:
    user_name = input('Enter username: ').strip().lower()
    if user_name not in accounts:
        print('Check username and try again bye')
        continue
    # if user_name in accounts:
    attempts = 1
    while attempts == 1:
        password = input('Enter password: ')
        if accounts[user_name] == password:
            print('Login succesfully')
            exit()
    else:
        print('Invalid login')
