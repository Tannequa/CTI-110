# Tannequa Whitehead
# 09/25/2026
# P2HW1
# This program calculates and displays travel expenses

print("This program calculates and display travel expenses")
print()

# Get the user's travel budget
budget = float(input("Enter Budget: "))

print()

# Get the user's travel destination
destination = input("Enter your travel destination: ")

print()

# Get the estimated gas expense
gas = float(input("How much do you think you will spend on gas? "))

# Get the estimated accommodation expense
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))

# Get the estimated food expense
food = float(input("Last, how much do you need for food? "))

# Add all travel expenses
total_expenses = gas + accommodation + food

# Subtract the expenses from the initial budget
remaining_balance = budget - total_expenses

print()
# Display the results
print("------- Travel Expenses -------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:.2f}")
print()
print(f"{'Fuel:':<20}${gas:.2f}")
print(f"{'Accommodation:':<20}${accommodation:.2f}")
print(f"{'Food:':<20}${food:.2f}")
print("-----------------------------")
print(f"{'Remaining Balance:':<20}${remaining_balance:.2f}")