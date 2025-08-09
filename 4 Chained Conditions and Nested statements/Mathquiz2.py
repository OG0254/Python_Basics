# Ask 4 different math questions

# Check if the answer is correct

# Keep track of the score

# Show a final result with feedback

print("\n--- Welcome to the Math Quiz ---")

name = input("Enter your name: ")
score = 0  # Score counter

# Question 1 (Addition)
q1 = int(input("1. What is 12 + 7? "))
if q1 == 19:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 19")

# Question 2 (Subtraction)
q2 = int(input("2. What is 25 - 9? "))
if q2 == 16:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 16")

# Question 3 (Multiplication)
q3 = int(input("3. What is 6 × 4? "))
if q3 == 24:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 24")

# Question 4 (Division)
q4 = float(input("4. What is 20 ÷ 5? "))
if q4 == 4:
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 4")

# Display Final Score
print("\n--- Quiz Completed ---")
print(f"{name}, your final score is: {score} out of 4")

# Bonus: Feedback based on score
if score == 4:
    print("🏆 Perfect! You're a math genius!")
elif score == 3:
    print("👍 Great job! Almost perfect.")
elif score == 2:
    print("😊 Not bad! Keep practicing.")
elif score == 1:
    print("🤔 You need some more practice.")
else:
    print("😢 Better luck next time! Keep learning.")

