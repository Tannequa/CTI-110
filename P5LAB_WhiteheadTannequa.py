# Tannequa Whitehead
# P5LAB
# 11/15/2026
# This program calculates the most efficient number of dollar and cent.

import random

def disperse_change(change):
    # Converting the value to an integer
    change = int(round(change * 100))
    
    # Determine how many coins are needed
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change

    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} Nickel")
        else:
            print(f"{num_nickels} Nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} Penny")
        else:
            print(f"{num_pennies} Pennies")

# Define the main function
def main():
    
    # Generate a random purchase amount
    amount_owed = round(random.uniform(0.01, 100.00), 2)

    # Display the amount owed
    print(f"Amount owed: ${amount_owed:.2f}")

    # Get the amount of cash from the customer
    cash = float(input("Enter amount of cash: $"))

    # Calculate the change owed
    change = round(cash - amount_owed, 2)

    # Display the change if enough cash was entered
    if cash >= amount_owed:
        print(f"Change owed: ${change:.2f}")

        # Display the dollars and coins
        disperse_change(change)
    else:
        print("Not enough cash to complete the purchase.")


#  Call the main funtion
if __name__ == "__main__":
    main()