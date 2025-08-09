class EqualToError(Exception):
    pass

amount = input("Enter amount to pay: ")
try:
    total = int(amount)
    if total <= 0:
        raise EqualToError("Amount must be greater than 0")
    print(f"Payment of {total} accepted")
except ValueError:
    print("Invalid entry")
except EqualToError:     #or except EqualToError as e:
    print("Amount must be greater than 0")        #or print(e)
finally:
    print("Transaction complete")