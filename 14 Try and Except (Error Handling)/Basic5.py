import logging

logging.basicConfig(
    filename = 'atm_transactions.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

class InsufficientFundsError(Exception):
    pass
class NegativeNumberError(Exception):
    pass

total_used = 0
balance = 10000
while True:
    try:
        withdraw = int(input("Enter amount to withdraw: "))
        if withdraw > balance:
            raise InsufficientFundsError(f"Attempted to withdraw {withdraw} with balance {balance}")
        if withdraw < 0:
            raise NegativeNumberError(f"Attempted to withdraw {withdraw} error!")
        final_balance = balance - withdraw
        logging.info(f"The initial balance is {balance} and withdrew amount is {withdraw}, final balance {final_balance}")
        print(f"Initial balance {balance}")
        print(f"Final balance is {final_balance}")
        # total_used = balance - final_balance
        balance = final_balance
        total_used += withdraw
        more = input("Do you want to add another transaction? (yes/no): ")
        if more.lower() != "yes":
            break
        # print(f"Total amount withdrawn {total_used}")
        # print(f"Final account balance {balance}")
    except ValueError:
        print("Invalid Entry")
        logging.error("Invalid data")
    except InsufficientFundsError as e:
        print(e)
        logging.error(e)
    except NegativeNumberError as e:
        print(e)
        logging.error(e)
    finally:
        print("Session end")
        logging.info("Session end")
print(f"Total amount withdrawn {total_used}")
print(f"Final account balance {balance}")