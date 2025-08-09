import logging

logging.basicConfig(
    filename='system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DivideByZeroError(Exception):
    pass

try:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    if num2 == 0: 
        raise DivideByZeroError("You cannot divide by zero!")
    result = num1 / num2
    print(result)
except ValueError:
    print("Input a valid number")
    logging.error("Invalid number entered")
except DivideByZeroError as e:
    print(e)
    logging.error(f"Division by zero attempted: num1={num1}, num2={num2}")
finally:
    print("Calculation complete!")
    logging.info("Calculation process completed.")
