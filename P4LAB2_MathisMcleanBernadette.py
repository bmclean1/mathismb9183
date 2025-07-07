 def display_table(n):
 for i in range(1, 12):
print(f"{n} * {i} = {n * i}")

run_program = "yes"
 while run_program.lower() == "yes":
try:
 number = int(input("\nEnter an integer: "))
if number >= 0:
 display_table(number)
   else:
 # Still display table for 0 and show the message
 display_table(0)
 print("Invalid input. Please enter a valid integer.")
 run_program = input("\nWould you like to run the program again? ")
 print("Exiting Program...")
