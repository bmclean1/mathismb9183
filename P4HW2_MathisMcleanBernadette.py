# Title: Python 4 - Loops
# Your Name: Bernadette Mathis Mclean
# Date: 7/7/2025
# Assignment Name: Introduction to Python Mod 6 P4HW2
# A brief description of the project: The program calculates gross pay for multiple employees,
# including totals for overtime, regular pay, gross pay, and number of employees.

# Initialize accumulators
employee_count = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

while True:
    employee_name = input('\nEnter employee\'s name or "Done" to terminate: ')
    if employee_name == "Done":
        break

    try:
        hours_worked = float(input(f"How many hours did {employee_name} work? "))
        pay_rate = float(input(f"What is {employee_name}'s pay rate? "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    # Calculate pay
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = hours_worked

    overtime_pay = overtime_hours * pay_rate * 1.5
    regular_pay = regular_hours * pay_rate
    gross_pay = regular_pay + overtime_pay

    # Display individual employee summary
    print(f"\nEmployee name: {employee_name}")
    print("Hours Worked  Pay Rate    OverTime    OverTime Pay  RegHour Pay   Gross Pay")
    print("--------------------------------------------------------------------------")
    print(f"{hours_worked:<13.1f}{pay_rate:<11.2f}{overtime_hours:<11.1f}"
          f"{overtime_pay:<14.2f}${regular_pay:<12.2f}${gross_pay:.2f}")

    # Update totals
    employee_count += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

# Display summary
print(f"\nTotal number of employees entered: {employee_count}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")

