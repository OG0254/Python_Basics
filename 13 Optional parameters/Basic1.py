# def calculate_salary(x , y = 0, z = 0):
#     print(x)
#     if y == 0 or z == 0:
#         print(x)
#     elif z == 0:
#         print(x + y)
#     # else:
#     #     print(net_salary)
#     #return x + y + z
# x = int(input("Enter basic salary: "))
# y = int(input("Enter allowance: "))
# z = int(input("Enter bonus: "))
# net_salary = x + y + z
# #calculate_salary(x , y, z)
# print("Payslip")
# print("--------------------")
# print(f"Total salary is {net_salary}")

def calculate_salary(basic_salary, allowance=0, bonus=0):
    total = basic_salary + allowance + bonus
    print("Payslip")
    print("--------------------")
    print(f"Basic Salary: {basic_salary}")
    print(f"Allowance: {allowance}")
    print(f"Bonus: {bonus}")
    print("--------------------")
    print(f"Total Salary: {total}")

# Example calls
calculate_salary(50000)
calculate_salary(50000, 5000)
calculate_salary(50000, 5000, 10000)
