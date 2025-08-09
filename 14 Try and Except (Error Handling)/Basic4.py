class InsufficientFundsError(Exception):
    pass

import logging

logging.basicConfig(
    filename='transaction.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    deposit = int(input("Enter amount to deposit: "))
    withdraw = int(input("Enter amount to withdraw: "))

    if withdraw > deposit:
        raise InsufficientFundsError("You have insufficient funds")
    total = deposit - withdraw
    logging.info(f"Deposited: {deposit}, Withdrew: {withdraw}, Balance: {total}")
    print(f"Balance amount is {total}")
except ValueError:
    print("Invalid entry!")
    logging.error("Invalid entry!")
except InsufficientFundsError as e:
    print(e)
    logging.error(e)
finally:
    print("Session closed!")
    logging.error("Session closed!")