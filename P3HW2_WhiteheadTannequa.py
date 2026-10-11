# Tannequa Whitehead
# 10/10/2026
# P3HW2
# This program calculate employee paye rate, overtime pay, and gross pay

# Pseudocode:
# Get the employee's name, hours worked, and pay rate.
# If hours worked are greater than 40:
#     Calculate overtime hours as hours worked minus 40.
#     Calculate ovetime pay using 1.5 times the pay rate.
#     Calculate regular pay for 40 hours.
# Otherwise:
#     Set overtime hours and overtime pay to zero.
#     Calculate regular pay for hours worked.
# Add regular pay and overtime pay to get gross pay
# Display the employee's name and aligned payroll results.

# Get employee information
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's rate: "))

# Calculate regular and overtime pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display results
print("----------------------------------------")
print(f"Employee name:       {employee_name}")
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<15}" 
      f"{'Overtime':<15}{'Overtime Pay':<18}" 
      f"{'RegHour Pay':<18}{'Gross Pay':<15}")
print("-" * 95)
print(f"{hours_worked:<15.2f}{pay_rate:<15.2f}"
      f"{overtime_hours:<15.2f}{overtime_pay:<18.2f}"
      f"${regular_pay:<17.2f}${gross_pay:.2f}")