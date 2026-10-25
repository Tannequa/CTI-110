# Tannequa Whitehead
# 10/24/2026
# P4LAB2
# This program display a multiplication table and allow the user to run again.

# Pseudocode:
# Set run_again to "yes".
# Repeat the program while run_again is not "no".
#       Ask the user to enter an integer.
#       If the integer is zero or greater:
#          Use a for loop to count from 1 through 12.
#          Multiply the user's integer by each count.
#          Display each multiplication equation and result.

#       Otherwise:
#           Display a message that negative values are not accepted.
#       Ask the user if they want to run program again.
#       Store their answer in run_again.
#       If the answer is "yes", repeat.
#       If the answer is "no", exit the loop.
# Display a message that the program is ending

print("Tannequa Whitehead")

run_again = "yes"

while run_again != "no":
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        # Display multiplication table from 1 to 12
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print("This program does not handle negative values")
    
    run_again = input("Would you like to run the program again? ")

# Loop has ended because the user entered "no"
print("Program is ending....")