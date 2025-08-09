print("\n--- Welcome to the Math Quiz ---")

name = input("Enter your name: ")
score = 0  # Initialize score

# Question 1
q1 = int(input("1. What is 5 + 3? "))
if q1 == 8:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 8")

# Question 2
q2 = int(input("2. What is 10 - 4? "))
if q2 == 6:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 6")

# Question 3
q3 = int(input("3. What is 3 * 3? "))
if q3 == 9:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 9")

# Final Result
print("\n--- Quiz Completed ---")
print(f"{name}, your final score is: {score} out of 3")

# Optional bonus feedback
if score == 3:
    print("Excellent! You got all answers right.")
elif score == 2:
    print("Good job! You got most of them.")
elif score == 1:
    print("You need more practice.")
else:
    print("Try again. Don't give up!")
