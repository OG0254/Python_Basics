# Imagine you're building a basic system for a fuel station. A user can keep fueling up and entering how many liters they want. The system calculates the cost and updates the total bill. When they're done, they type 'stop'.

# 🛠️ Sample Requirements:
# Ask the user to enter liters of fuel (or 'stop' to finish).

# Fuel costs, say, Ksh 180 per liter.

# Keep adding to the total.

# When done, print a receipt with:

# Total liters fueled

# Total cost

# Number of fueling attempts

print('--- Fuel Station Pump" Simulator ---\n')

fuel_cost = 180
attempts = 0
total_liters = 0
total_bill = 0
while True:
    liters = int(input("Enter liters of fuel (or '0' to finish): "))
    if liters == 0:
        break
    attempts += 1
    total_liters += liters
    total_cost = fuel_cost * liters
    total_bill += total_cost
    print(f'Total bill: {total_bill}')

    # fuel_cost = 180

print(f'\n🧾 Receipt:')
print(f'Total liters: {total_liters}')
print(f'Total cost per liter is : {fuel_cost}')
print(f'Total bill: {total_bill}')
print(f'Number of fueling attempts: {attempts}')
