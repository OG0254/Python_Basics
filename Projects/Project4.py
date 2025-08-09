print("Ogada Simple Phonebook Manager\n")

print("User Interface: ")
print("1. Add New Contact")
print("2. View All Contacts")
print("3. Search for a Contact")
print("4. Exit")

contact_names = []
contact_numbers = []

while True:
    choice = int(input("Enter choice 1/2/3/4: "))
    if choice == 1:
        name = input("Enter name: ").strip().title()
        number = input("Enter number: ")
        # for name, numbers in zip(contact_names, contact_numbers):
        #     print(name, numbers)
        contact_names.append(name)
        contact_numbers.append(number)
        print("Contact added successfully!")
        more = input("Do you want to enter a new choice? (yes/no) ")
        if more.lower() != "yes":
            break

    elif choice == 2:
        if contact_names:
            for name, numbers in zip(contact_names, contact_numbers):
                print(name, numbers)
        else:
            print("Contact not available")
        more = input("Do you want to enter a new choice? (yes/no) ")
        if more.lower() != "yes":
            print("Typo check answer!")
            break

    elif choice == 3:
        while True:
            name = input("Enter name to search: ").strip().title()
            if name in contact_names:
                position = contact_names.index(name)
                print(name, contact_numbers[position])

                # saved_name = input("Enter name to search: ")
                # for saved_name, numbers in zip(contact_names, contact_numbers):
                # contact_names == saved_name
                # print(contact_names, contact_numbers)
            # if contact_names != name:
            else:
                print("Contact not available")
            # name = str(input("Enter the contact name: ")).strip().title()
            # if name in contact_names:
            #     for name, numbers in zip(contact_names, contact_numbers):
            #         # index = contact_names.index(name), contact_numbers.index(number)
            #         print(name, number)
            # else:
            #     print("Contact not available")
            break
        more = input("Do you want to enter a new choice? (yes/no) ")
        if more.lower() != "yes":
            print("Typo check answer!")
            break

    else:
        choice == 4
        print("Goodbye")
        break
