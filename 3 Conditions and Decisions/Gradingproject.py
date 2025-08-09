# Write a program that:

# Asks the user to enter their exam score (0–100)
# Decides and prints the grade:
# 70–100 = A
# 60–69 = B
# 50–59 = C
# 40–49 = D
# 0–39 = F


# Code


print('\n--- Grades ---')
print('70-100 = A')
print('60-69 = B')
print('50-59 = C')
print('40-49 = D')
print('0-39 = F')

score = int(input('Enter exam score: '))

if score >= 70 and score <= 100:
    print('A')
elif score >= 60:
    print('B')
elif score >= 50:
    print('C')
elif score >= 40:
    print('D')

else:
    print('F')
