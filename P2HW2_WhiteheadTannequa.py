# Tannequa Whitehead
# 09/22/2026
# P2HW2
# This program will ask user to enter test grades using a separate input statement

# Get six inputs from user 
Module1 = float(input("Enter grade for first module:"))
Module2 = float(input("Enter grade for second module:"))
Module3 = float(input("Enter grade for third module:"))
Module4 = float(input("Enter grade for fourth module:"))
Module5 = float(input("Enter grade for fifth module:"))
Module6 = float(input("Enter grade for sixth module:"))

# Create a list holding user inputs
grades = [Module1, Module2, Module3,Module4, Module5, Module6]

# Print the list
print(grades)

# Get the number of items in  the list
print()
print(f"Total of number of items in list: {len(grades)}")

# Use the sum function to add all grades in the list
total_grade = sum(grades)

# Use the average function to get grade average
average = total_grade/len(grades)

# Display total grade
print()
print(f"The lowest value in the list is: {min(grades):.2f}")
print()
print(f"The highest value in the list is: {max(grades):.2f}")
print()
print(f"Total sum for all grades are: {total_grade:.2f}")
print()
print(f"The average for all the grades are: {average:.2f}")


