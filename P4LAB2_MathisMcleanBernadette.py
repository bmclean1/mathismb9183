Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def display_table(n):
...     for i in range(1, 12):
...         print(f"{n} * {i} = {n * i}")
...
... run_program = "yes"
...
... while run_program.lower() == "yes":
...     try:
...         number = int(input("\nEnter an integer: "))
...         if number >= 0:
...             display_table(number)
...         else:
...             # Still display table for 0 and show the message
...             display_table(0)
...
...         print("Invalid input. Please enter a valid integer.")
...
...     run_program = input("\nWould you like to run the program again? ")
...
... print("Exiting Program...")
