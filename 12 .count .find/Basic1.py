filename = input("Enter the filename to open: ")

try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
    exit()

word = input("Enter a word to count: ")
count = content.count(word)
print(f"The word '{word}' appears {count} times in the file.")
