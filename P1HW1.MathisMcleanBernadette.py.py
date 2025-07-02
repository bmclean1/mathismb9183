# Your Name:Your Name: Bernadette Mathis Mclean
# Date: 6/16Date: 6/16/2025
# Assignment Name: Introduction to Python 3
# A brief Description of the project:
# This assignment tests knowledge of how to write code that collects information from users,
# processes the information collected, and displays results to other users.

# Power calculation
base = int(input("Enter an integer value at the base: "))
exponent = int(input("Enter an integer as the exponent: "))
power_result = base ** exponent
print(f"{base} raised to the power of {exponent} is {power_result}")

# Addition and subtraction
starting_value = int(input("\nEnter a starting integer: "))
add_value = int(input("Enter an integer to add: "))
subtract_value = int(input("Enter an integer to subtract: "))
final_result = starting_value + add_value - subtract_value
print(f"{starting_value} + {add_value} + {-subtract_value} is equal to {final_result}")


Using Python's input and print functions, you will create a program that shows
output similar to below.
Since you created a Github account in the last assignment, try coding this
program in Github Codespaces. See the "IDE" document in the "Course Resources"
folder for more information on Github Codespaces.

#enter a integer value at the base of: 7
#enter integer as the  exponent: 3

7 raised to the power of 3 is 343 !!

Addition and subtraction Enter a starting integer:10

#Enter an integer to add: 6
#Enter an integer to subtraction: 4

10+6+-4 is equal to 12

Recreate the output shown above. Do NOT hardcode the integers.
The values should be able to change each time the program runs.
In other words, any numbers should work, not just the ones shown in
the example. The user should be able to enter any integer for the
base value and the exponent. Then print the string showing the base,
exponent, and the result. Don't forget the exclamation points.
Next, the user should enter three separate integers. The first two
integers should be added together. Then the last given integer
should be subtracted from the sum of the other two numbers.
Your output should look as close as possible to the output shown above.
