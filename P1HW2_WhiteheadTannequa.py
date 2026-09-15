# Tannequa Whitehead
# 09/12/2026
# P1HW2
# This program calculates and displays travel expenses

print("This program calculates and display travel expenses")
print()

# Get the user's travel budget
budget = int(input("Enter Budget: "))

print()

# Get the user's travel destination
destination = input("Enter your travel destination: ")

print()

# Get the estimated gas expense
gas = int(input("How much do you think you will spend on gas? "))

# Get the estimated accommodation expense
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))

# Get the estimated food expense
food = int(input("Last, how much do you need for food? "))

# Add all travel expenses
total_expenses = gas + accommodation + food

# Subtract the expenses from the initial budget
remaining_balance = budget - total_expenses

print()
# Display the results
print("------- Travel Expenses -------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)