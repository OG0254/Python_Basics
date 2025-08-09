# username = "Ogada"
# password = "Vital1"
attempts = 0

# name = input("Enter a username: ")
# if name == "Ogada":
#     print("Check username an try again")
#     attempts += 1
while True:
    name = input("Enter a username: ")
    if name == "Ogada":
        # attempts += 1
        print("Username correct")
        break
        # attempts += 1
        # if name == "Ogada":
        # continue
    else:
        print("Check the username and try again!")
        # break
while True:
    password = input("Enter password: ")
    if password == "Vital1":
        print("Login successful!")
        break
    else:
        print("Invalid password")
        # break
