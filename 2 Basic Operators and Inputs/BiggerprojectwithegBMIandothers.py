

# 1. Simple Interest Calculator - Formulas are given 
# 2. BMI Calculator  - Formulas are given 
# 3. Travel Cost Estimator - Formulas are given 




# Sample Code of how it would look like but here its not repetitive the below code will now be repetitive until the user exits

print("--- Multi-Tool Mini App ---")

print("\nChoose a calculator:")
print("1. Simple Interest Calculator")
print("2. BMI Calculator")
print("3. Travel Cost Estimator")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    # Simple Interest Calculator
    print("\n--- Simple Interest Calculator ---")
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (%): "))
    time = float(input("Enter time (in years): "))

    interest = (principal * rate * time) / 100
    print(f"Simple Interest: {interest}")

elif choice == '2':
    # BMI Calculator
    print("\n--- BMI Calculator ---")
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (meters): "))

    bmi = weight / (height ** 2)
    print(f"Your BMI is: {round(bmi, 2)}")

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 25:
        print("You have a normal weight.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

elif choice == '3':
    # Travel Cost Estimator
    print("\n--- Travel Cost Estimator ---")
    distance = float(input("Enter travel distance (km): "))
    fuel_price = float(input("Enter fuel price per liter: "))
    fuel_efficiency = float(input("Enter vehicle fuel efficiency (km per liter): "))

    total_fuel_needed = distance / fuel_efficiency
    total_cost = total_fuel_needed * fuel_price

    print(f"Total Fuel Needed: {round(total_fuel_needed, 2)} liters")
    print(f"Estimated Travel Cost: {round(total_cost, 2)}")

else:
    print("Invalid choice. Please choose 1, 2, or 3.")



# we use while loop for it to be repetitive

while True:
    print("\n--- Multi-Tool Mini App ---")
    print("Choose a calculator:")
    print("1. Simple Interest Calculator")
    print("2. BMI Calculator")
    print("3. Travel Cost Estimator")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        # Simple Interest Calculator
        print("\n--- Simple Interest Calculator ---")
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (%): "))
        time = float(input("Enter time (in years): "))

        interest = (principal * rate * time) / 100
        print(f"Simple Interest: {interest}")

    elif choice == '2':
        # BMI Calculator
        print("\n--- BMI Calculator ---")
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (meters): "))

        bmi = weight / (height ** 2)
        print(f"Your BMI is: {round(bmi, 2)}")

        if bmi < 18.5:
            print("You are underweight.")
        elif bmi < 25:
            print("You have a normal weight.")
        elif bmi < 30:
            print("You are overweight.")
        else:
            print("You are obese.")

    elif choice == '3':
        # Travel Cost Estimator
        print("\n--- Travel Cost Estimator ---")
        distance = float(input("Enter travel distance (km): "))
        fuel_price = float(input("Enter fuel price per liter: "))
        fuel_efficiency = float(input("Enter vehicle fuel efficiency (km per liter): "))

        total_fuel_needed = distance / fuel_efficiency
        total_cost = total_fuel_needed * fuel_price

        print(f"Total Fuel Needed: {round(total_fuel_needed, 2)} liters")
        print(f"Estimated Travel Cost: {round(total_cost, 2)}")

    elif choice == '4':
        print("Thank you for using the Multi-Tool App. Goodbye! 👋")
        break  # exit the loop and stop the program

    else:
        print("Invalid choice. Please select 1, 2, 3 or 4.")
