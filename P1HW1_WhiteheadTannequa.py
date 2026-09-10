# Tannequa Whitehead
# 09/10/2026
# Inputs, outputs, and mathematical calculations

print("------- Calculating Exponents -------")
print()
print()

# Get base value from use and convert to int
base_value = int(input ("Enter a base value: "))

# Get exponent from use and convert to int
exponent = int(input ("Enter an exponent: "))

# Calculate
answer = base_value ** exponent

# Display the answer
print(base_value, "raise to the power of", exponent, "is", answer)
print()
print()

print("------- Addition and Subtraction -------")
print()
print()

# Get three integers from user
num1 = int(input("Enter starting number: "))
num2 = int(input("Enter number to add: "))
num3 = int(input("Enter number to subtract: "))

print()

# Display results
print(num1, "+", num2, "-", num3, "=", num1 + num2 - num3)