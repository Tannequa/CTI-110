# Tannequa Whitehead
# 10/27/2026
# P4HW1
# This program will collect test scores, validate them, remove the lowest score, calculate the average, and display a letter grade.

# Ask user for the number of scores 
number_scores = int(input("How many scores do you want to enter? "))

# Create a list to hold the scores
scores = []

# Collect and validate each score
for count in range(number_scores):
    score = float(input(f"Enter score #{count +  1}: "))

    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{count + 1} again: "))

# Add valid score to the list
    scores.append(score)
    
# Find the lowset score
lowest_score = min(scores)

# Remove the lowest score from the list
scores.remove(lowest_score)

# Calculate the average of the modified list
average = sum(scores) / len(scores)

# Dtermine the letter grade
if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the resluts
print()
print("--------------Results-------------")
print()
print(f"Lowest Score : {lowest_score}")
print()
print(f"Modified List : {scores}")
print()
print(f"Scores Average: {average:.2f}")
print(f"Grade        : {letter_grade}")
print("-----------------------------------")


