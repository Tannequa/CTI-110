# Tannequa Whitehead
# 10/10/2026
# P3HW1
# This program collects six module grades and display statistics and a letter grade.

# Pseudocode:
# Input six grades as decimal numbers.
# Store all six grades in a list.
# Calculate the lowest, highest, sum, average.
# Display the results, formatting the average to two decimal places
# Determine and display the letter grade: 90 or higher = A, 80 or higher = B, 70 or higher = C, 60 or higher = D, below 60 = F.

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# Add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
sum = sum(grades)
avg = sum / len(grades)

# Display results
print("\n----------Results------------")
print(f"{'Lowest Grade:':<20}{low:.1f}")
print(f"{'Highest Grade:':<20}{high:.1f}")
print(f"{'Sum of Grades:':<20}{sum:.1f}")
print(f"{'Average Grade:':<20}{avg:.1f}")

# Determine letter grade for average
if avg >= 90:
    print("Your grade is: A")
else:
    if avg >= 80:
        print("Your grade is: B")
    else:
        if avg >= 70:
            print("Your grade is: C")
        else:
            if avg >= 60:
                print("Your grade is: D")
            else:
                print("Your grade is: F")




