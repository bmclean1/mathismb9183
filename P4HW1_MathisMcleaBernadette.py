# Your Name: Bernadette Mathis Mclean
# Date: 7/7/2025
# Assignment Name: Introduction to Python 4 Mod 7 P4HW1
# Description: Create a Python code file using a form

# -------------------------------- Pseudocode --------------------------------
# 1. Ask user how many scores they want to enter
# 2. Initialize an empty list to store valid scores
# 3. Use a loop to repeat until all scores are collected:
#     a. Ask user to enter a score
#     b. Check if the score is between 0 and 100
#         - If valid, add it to the list
#         - If invalid, print a warning and prompt again (repeat step b)
# 4. After collecting all scores:
#     a. Find the lowest score
#     b. Create a new list without the lowest score
#     c. Calculate the average of the modified list
#     d. Determine the letter grade based on the average
# 5. Display:
#     - Lowest score
#     - Modified list
#     - Average score (formatted to 2 decimal places)
#     - Letter grade
# ------------------------------------------------------------------

# Ask how many scores the user wants to enter
num_scores = int(input("How many scores do you want to enter? "))

# List to store valid scores
score_list = []

# Collect scores
for i in range(1, num_scores + 1):
    while True:
        try:
            score = float(input(f"Enter score #{i}: "))
            if 0 <= score <= 100:
                score_list.append(score)
                break
            else:
                print("\nINVALID Score entered !!!!")
                print("Score should be between 0 and 100")
        except ValueError:
            print("\nINVALID input! Please enter a valid number.")

# Process scores
lowest_score = min(score_list)
score_list.remove(lowest_score)
average_score = sum(score_list) / len(score_list)

# Determine letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display results
print("\n------------Results----------------")
print(f"Lowest Score : {lowest_score}")
print(f"Modified List: {score_list}")
print(f"Scores Average: {average_score:.2f}")
print(f"Grade: {letter_grade}")
print("-----------------------------------")

