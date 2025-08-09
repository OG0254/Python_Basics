rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):  # outer loop for rows
    for j in range(i):  # inner loop for printing (*)
        print("*", end=" ")
    print()  # move to the next line after inner loop
