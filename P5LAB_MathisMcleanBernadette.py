# Title: Python 7 - Use of loops, functions and module import to complete assignments
# Your Name: Bernadette Mathis Mclean
# Date: 7/10/2025
# Assignment Name: Introduction to Python Mod 7 P5LAB
# A brief description of the project: This program simulates a customer using a self-checkout machine. A random float value is generated as the total owed for the purchase. The user inputs their payment, and the program calculates and displays the dollar and coin change using a function called disperse_change.

import random

def disperse_change(change):
    # Convert change from dollars to cents to avoid float rounding issues
    cents = round(change * 100)

    denominations = {
        "Dollars": 100,
        "Quarters": 25,
        "Dimes": 10,
        "Nickels": 5,
        "Pennies": 1
    }

    print("\nChange breakdown:")
    for name, value in denominations.items():
        count = cents // value
        cents %= value
        print(f"{name}: {count}")

def main():
    # Generate a random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")

    # Prompt user for cash input
    cash_inserted = float(input("How much cash will you put in the self-checkout? $"))

    # Check for sufficient payment
    if cash_inserted < total_owed:
        print("Insufficient amount. Please insert more money.")
        return

    # Calculate and display change
    change_due = round(cash_inserted - total_owed, 2)
    print(f"Change is ${change_due:.2f}")

    # Call the function to break down the change
    disperse_change(change_due)

# Run the main function
main()